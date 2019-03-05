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

import binascii
import os
import hmac
import hashlib
import socket
import sys
import dtlv
from collections import OrderedDict
import json
import logging

sys.path.append(os.path.join(os.path.split(__file__)[0], './dict'))
from metadict import *

PACKET_SIZE = 8192
DEFAULT_PORT = 3901

class Packet:
    CMD_CODE_AUTH = 1
    CMD_CODE_TERMINATE = 2
    CMD_CODE_SRVMSG = 3
    CMD_CODE_NTFMSG = 4

    CMD_FLAG_REQUEST = 1 << 7
    CMD_FLAG_SECURED = 1 << 6
    CMD_FLAG_ERROR = 1 << 5

    def __init__(self, serviceId=0, flags=0, identifier=1, code=0, data=None, avplist=None):
        self.serviceId = serviceId
        self.code = code
        self.flags = flags
        self.identifier = identifier
        self.length = 0
        self.avplist = avplist
        self.data = data
        self.auth = None
        self.digest = None

    def encode(self, secret, advauth=None):
        comp = [ dtlv.word_to_hex(self.serviceId), '0'*4, # Service-Id, Length 
                 dtlv.byte_to_hex(self.flags), dtlv.byte_to_hex(self.code), dtlv.word_to_hex(self.identifier), # Flags, Code, Identifier
               ]
        if self.isAuthRequest():
            comp.append('0'*64) # digest
            self.auth = binascii.b2a_hex(os.urandom(32)).decode()
            comp.append(self.auth) # Authenticator
        else:
            comp.append(advauth)

        if self.avplist:
            comp.append(self.avplist.encode())

        self.length = sum(map(lambda x: len(x), comp))/2
        comp[1] = dtlv.word_to_hex(self.length)

        data = binascii.unhexlify(''.join(comp))
        h = hmac.new(secret.encode(), data, hashlib.sha256)
        self.digest = binascii.hexlify(h.digest()).decode()
        comp[5] = self.digest

        self.data = ''.join(comp)
        return self.data

    def isAuthRequest(self):
        return self.code == Packet.CMD_CODE_AUTH

    def decode(self, secret):
        self.serviceId = int(self.data[0:4], 16)
        self.length = int(self.data[4:8], 16)
        self.flags = int(self.data[8:10], 16)
        self.code = int(self.data[10:12], 16)
        self.identifier = int(self.data[12:16], 16)
        self.digest = self.data[16:80]
        hdrlen = 80
        if self.isAuthRequest():
            self.auth = self.data[80:144]
            hdrlen = 144

        self.avplist = dtlv.AVPList(data=self.data[hdrlen:], context_ns_id=udpctl.namespace_id)
        self.avplist.decode()

class UdpControlClient():

    def __init__(self, secret, host, port=DEFAULT_PORT, timeout=2, bind_addr='0.0.0.0', bind_port=DEFAULT_PORT):
        self.secret = secret
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((bind_addr, port))
        self.s.settimeout(timeout)
        self.packet_id = 0
        self.advAuth = None

    def auth(self):    
        self.packet_id = 1
        packet = Packet(serviceId=udpctl.namespace_id, flags=Packet.CMD_FLAG_REQUEST | Packet.CMD_FLAG_SECURED, identifier=self.packet_id, code=Packet.CMD_CODE_AUTH)
        self.sendPacket(packet)
        packet = self.recvPacket()
        return packet

    def srvmsg(self, message, serviceId):
        avplist = dtlv.AVPList()
        avplist.from_json_serializable(message)

        self.packet_id += 1
        packet = Packet(serviceId=serviceId, flags=Packet.CMD_FLAG_REQUEST | Packet.CMD_FLAG_SECURED, identifier=self.packet_id, code=Packet.CMD_CODE_SRVMSG, avplist=avplist)

        self.sendPacket(packet)
        packet = self.recvPacket()
        return packet

    def sendPacket(self, packet):
        data = packet.encode(self.secret, advauth=self.advAuth)
        logging.debug('send: id:%d, code:%d, service:%d, digest:%s', packet.identifier, packet.code, packet.serviceId, packet.digest)
        if packet.avplist:
            logging.debug('send_packet:\n%s', json.dumps(packet.avplist.as_json_serializable(), indent=4, separators=(',', ': ')) )

        logging.debug('send_data: %s', data)
        data = binascii.unhexlify(data)
        self.s.sendto(data, (self.host, self.port))

    def recvPacket(self, rerror=True):
        while True:
            data, addr = self.s.recvfrom(PACKET_SIZE)
            data = binascii.hexlify(data)

            logging.debug('recv_data: %s', data)
            packet = Packet(serviceId=0, flags=Packet.CMD_FLAG_SECURED, identifier=1, code=Packet.CMD_CODE_AUTH, data=data)
            packet.decode(self.secret)

            logging.debug('recv: id:%d, code:%d, service:%d, digest:%s', packet.identifier, packet.code, packet.serviceId, packet.digest)
            json_data = packet.avplist.as_json_serializable()
            logging.debug('recv_packet:\n%s', json.dumps(json_data, indent=4, separators=(',', ': ')) )

            if packet.code != Packet.CMD_CODE_NTFMSG:
                self.advAuth = packet.digest
                return packet
            else:
                logging.info('got notification: service:%d\n%s\n', packet.serviceId, json.dumps(packet.avplist.as_json_serializable(), indent=4, separators=(',', ': ')))
        return None