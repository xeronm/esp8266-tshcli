#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ESP8266 Things Shell UDP Control Protocol
# Copyright (c) 2018 Denis Muratov <xeronm@gmail.com>.
# https://dtec.pro/gitbucket/git/esp8266/esp8266-tsh.git
#
# This file is part of ESP8266 Things Shell Command Line Utility.
#
# ESP8266 Things Shell Command Line Utility is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
#

from collections import OrderedDict
import dtlvmeta
import binascii
import logging
from utility import *

class AVP:
    TYPE_OCTETS = 0
    TYPE_OBJECT = 1
    TYPE_INTEGER = 2
    TYPE_CHAR = 3

    def __init__(self, length=0, datatype=TYPE_OCTETS, islist=False, code=0, namespace_id=0, context_ns_id=0, data=None, avplist=None, value=None, fixed_length=None):
        self.length = length
        self.fixed_length = fixed_length
        self.datatype = datatype
        self.islist = islist
        self.code = code
        self.namespace_id = namespace_id
        self.context_ns_id = namespace_id or context_ns_id
        self.data = data
        self.avplist = avplist
        self.value = value

    @property
    def meta(self):
        return dtlvmeta.avpIndex.find(namespace_id=self.context_ns_id, code=self.code) or \
            dtlvmeta.avpIndex.find(namespace_id=0, code=self.code)

    @property
    def key(self):
        keystr = None
        meta = self.meta
        if meta:
            keystr = meta.fullName()
        else:
            keystr = '%d.%d' % (self.namespace_id, self.code)
        if self.namespace_id:
           moduleName = dtlvmeta.avpIndex.moduleById(self.namespace_id)
           if moduleName:
               keystr = '%s:%s' % (moduleName, keystr)

        return keystr

    def decodeHeader(self):
        length = int(self.data[0:4], 16)
        self.datatype = (length & 0xC000) >> 14
        self.islist = (length & 0x2000)
        self.length = (length & 0x1FFF)
    
        code = int(self.data[4:8], 16)
        self.namespace_id = (code & 0xFC00) >> 10
        self.code = code & 0x03FF

        self.context_ns_id = self.namespace_id or self.context_ns_id

    def decodeValue(self):
        self.value = None
        if self.islist or self.datatype == AVP.TYPE_OBJECT:
            self.value = self.avplist.avps
        elif self.datatype == AVP.TYPE_CHAR:
            self.value = binascii.unhexlify(self.data[8:-2])
        elif self.datatype == AVP.TYPE_OCTETS:
            self.value = binascii.unhexlify(self.data[8:])
        elif self.datatype == AVP.TYPE_INTEGER:
            self.value = int(self.data[8:], 16)
        else:
            self.value = '<error>'
        return self.value

    def as_json_serializable(self):
        value = None
        if self.islist or self.datatype == AVP.TYPE_OBJECT:
            value = self.avplist.as_json_serializable()
        elif self.datatype == AVP.TYPE_OCTETS:
            value = binascii.hexlify(self.value)
        else:
            value = self.value

        meta = self.meta
        if meta:
             value = meta.as_json_serializable(value)

        return value

    def from_json_serializable(self, value):
        if isinstance(value, list) or isinstance(value, dict):
            self.value = None
            self.avplist = AVPList(islist=isinstance(value, list))
            self.avplist.from_json_serializable(value)
        elif self.datatype == AVP.TYPE_OBJECT:
            raise Exception('Invalid value type for Object AVP')
        elif self.datatype == AVP.TYPE_OCTETS:
            self.value = binascii.unhexlify(value)
            self.avplist = None
        else:
            self.value = value
            self.avplist = None

    def encode(self):
        data = []

        value_data = None
        if self.islist or self.datatype == AVP.TYPE_OBJECT:
            value_data = self.avplist.encode(join=False)
        elif self.datatype == AVP.TYPE_CHAR:
            value_data = binascii.hexlify(self.value + '\0')
        elif self.datatype == AVP.TYPE_OCTETS:
            value_data = binascii.hexlify(self.value)
        elif self.datatype == AVP.TYPE_INTEGER:
            if self.fixed_length == 1:
                value_data = byte_to_hex(self.value)
            elif self.fixed_length == 2:
                value_data = word_to_hex(self.value)
            elif self.fixed_length == 4:
                value_data = int_to_hex(self.value)

        code = (self.code & 0x03FF) | ((self.namespace_id << 10) & 0xFC00)

        data = [ '0'*4, word_to_hex(code) ]
        if isinstance(value_data, list):
            data += value_data
        else:
            data.append(value_data)

        self.length = sum(map(lambda x: len(x), data))/2

        length = (self.length & 0x1FFF) | ((self.datatype << 14) & 0xC000)
        if self.islist:
            length |= 0x2000
        data[0] = word_to_hex(length)    

        allign_suffix = ((((self.length + 0b11) >> 2) << 2 ) - self.length)*2
        if allign_suffix:
            data.append('f'*allign_suffix)

        self.data = ''.join(data)
        return self.data


class AVPList:

    def __init__(self, data=None, avps=None, context_ns_id=0, islist=False):
        self.data = data
        self.avps = avps
        self.context_ns_id = context_ns_id
        self.islist = islist
        self.__pos = 0

    def __decode_avp(self):
        if self.__pos + 8 > len(self.data):
            raise Exception('Invalid length')

        avp = AVP(data=self.data[self.__pos:self.__pos + 8], context_ns_id=self.context_ns_id)
        self.__pos += 8
        avp.decodeHeader()

        data = self.data[self.__pos:self.__pos + avp.length*2 - 8]
        if ((avp.datatype == AVP.TYPE_OBJECT) or avp.islist):
            avp.avplist = AVPList(data=data, context_ns_id=avp.context_ns_id, islist=avp.islist)
            avp.avplist.decode()
        else:
            avp.data += data
            avp.decodeValue()
        self.__pos += ( (((avp.length + 0b11) >> 2) << 2 ) - 4 )*2

        return avp

    def decode(self):
        self.__decode_pos = 0
        avps = []
        while self.__pos < len(self.data):
            avp = self.__decode_avp()
            if not avp:
                return
            avps.append(avp)
        self.avps = avps
        return avps

    def as_json_serializable(self):
        obj = None
        if self.islist:
            obj = list([ x.as_json_serializable() for x in self.avps ])
        else:
            obj = OrderedDict([ (x.key, x.as_json_serializable()) for x in self.avps ])
        return obj

    def encode(self, join=True):
        avps = self.avps
        if isinstance(avps, OrderedDict) or isinstance(avps, dict):
            avps = list([ x for k,x in avps.items() ])
        data = []
        for avp in avps:
            data.append(avp.encode())
        if join:
            data = ''.join(data)
        return data


    def from_json_serializable(self, obj, listkey=None):
        if self.islist:
            objlist = [ (listkey, x) for x in obj ]
        else:
            objlist = [ (k, x) for k,x in obj.items() ]

        avps = []
        for key, value in objlist:
            namespace_id = 0
            key_wns = key.split(':')
            if len(key_wns) == 2:
                key = key_wns[1]
                module = dtlvmeta.avpIndex.moduleByName(key_wns[0])
                if module:
                    namespace_id = module.namespace_id
            meta = dtlvmeta.avpIndex.findByName(key)
            if not meta:
                logging.warning('from_json_serializable: AVP not found "%s"', key)
                continue

            avp = AVP(code=meta._code, namespace_id=namespace_id, datatype=meta._datatype, fixed_length=meta._fixed_length)
            avp.from_json_serializable(value)
            avps.append(avp)
        self.avps = avps
        return obj
