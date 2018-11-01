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

import inspect
import logging
import time
from utility import *

c_time_format = '%Y.%m.%d %H:%M:%S'

class datatype:
    TYPE_OCTETS = 0
    TYPE_OBJECT = 1
    TYPE_INTEGER = 2
    TYPE_CHAR = 3

class namespace:
    _namespace_id = 0
    _name = '<Abstract AVP Namespace>'

class baseAVP:
    _name = '<Abstract AVP>'
    _code = 0
    _namespace = namespace
    _module = None
    _fixed_length = None

    @classmethod
    def fullName(cls):
        return ''.join([cls._module or cls._namespace._name, '.', cls._name])

    @classmethod
    def as_json_serializable(cls, value):
        return value

class uint8(baseAVP):
    _datatype = datatype.TYPE_INTEGER
    _fixed_length = 1


class uint16(baseAVP):
    _datatype = datatype.TYPE_INTEGER
    _fixed_length = 2


class uint32(baseAVP):
    _datatype = datatype.TYPE_INTEGER
    _fixed_length = 4


class char(baseAVP):
    _datatype = datatype.TYPE_CHAR


class octets(baseAVP):
    _datatype = datatype.TYPE_OCTETS


class objectAVP(baseAVP):
    _datatype = datatype.TYPE_OBJECT

class date_time(uint32):

    @classmethod
    def as_json_serializable(cls, value):
        return time.strftime(c_time_format, time.localtime(value))

    @classmethod
    def from_json_serializable(cls, value):
        return math.trunc(time.strptime(c_time_format, str(value)))

class ptr24(uint32):

    @classmethod
    def as_json_serializable(cls, value):
        return '0x%06x' % value

    @classmethod
    def from_json_serializable(cls, value):
        return int(value, 16)

class ipv4_address(octets):
    _fixed_length = 4  

    @classmethod
    def as_json_serializable(cls, value):
        return hex_to_ipv4(value)

    @classmethod
    def from_json_serializable(cls, value):
        return ipv4_to_hex(value)

class mac48_address(octets):
    _fixed_length = 6

    @classmethod
    def as_json_serializable(cls, value):
        return hex_to_mac48(value)

    @classmethod
    def from_json_serializable(cls, value):
        return mac48_to_hex(value)

class time_zone(uint8):

    @classmethod
    def as_json_serializable(cls, value):
        return '%+02d:%02d' % (int(value/4), ((value)%4)*15)

    @classmethod
    def from_json_serializable(cls, value):
        return math.trunc(time.strptime(c_time_format, str(value)))

class AVP_Index:
    _idx = {}

    def __init__(self):
        self._index = {}
        self._nameIdx = {}
        self._moduleIdx = {}
        self._moduleNsidIdx = {}

    def addModule(self, module, moduleName = None):
        if not moduleName:
            moduleName = module.__name__

        if self._moduleIdx.get(moduleName):
            logging.error('AVPIndex:addModule: duplicate module name=%s', moduleName)
            return
        logging.info('AVPIndex:addModule: module name=%s', moduleName)
        self._moduleIdx[moduleName] = module

        if hasattr(module, 'namespace_id'):
            if self._moduleNsidIdx.get(module.namespace_id):
                logging.error('AVPIndex:addModule: duplicate module %s namespace_id=%d', moduleName, module.namespace_id)
                return
            logging.info('AVPIndex:addModule: module name=%s, namespace_id=%d', moduleName, module.namespace_id)
            self._moduleNsidIdx[module.namespace_id] = moduleName

        for (name, it) in module.__dict__.items():
            try:
                if not inspect.isclass(it) or not issubclass(it, baseAVP):
                    continue

                it._module = moduleName
                fullName = it.fullName()
                self._nameIdx[fullName] = it
                key = (it._namespace._namespace_id, it._code)

                item = self._index.get(key)
                if not item:
                    self._index[key] = it
                elif item._name != _it._name:
                    logging.warning('AVPIndex:addModule: duplicate AVP definition already indexed: ns=%d, code=%d, name=%s', _it._namespace._namespace_id, _it._code, _it._name)
                    logging.warning('AVPIndex:addModule: duplicate AVP definition try to index   : ns=%d, code=%d, name=%s', item._namespace._namespace_id, item._code, item._name)
            except:
                raise
                None

    def moduleByName(self, name):
        return self._moduleIdx.get(name)

    def moduleById(self, namespace_id):
        return self._moduleNsidIdx.get(namespace_id)

    def find(self, namespace_id=0, code=None):
        return self._index.get((namespace_id, code))

    def findByName(self, fullName):
        return self._nameIdx.get(fullName)

    def findEnumByName(self, fullName):
        idx = fullName.rfind('.')
        if idx == -1:
            return None
        enumName = fullName[idx+1:]
        fullName = fullName[:idx]
        avp = self._nameIdx.get(fullName)
       
        return getattr(avp, enumName)

avpIndex = AVP_Index()