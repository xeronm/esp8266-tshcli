#!/usr/bin/python
# -*- coding: utf-8 -*-

import dtlvmeta

class Message:
    INFO       = 1

class AppProduct(dtlvmeta.char):
    _name = 'Application-Product'
    _code = 1

class AppVersion(dtlvmeta.char):
    _name = 'Application-Version'
    _code = 2

class ResultCode(dtlvmeta.uint8):
    _name = 'Result-Code'
    _code = 3

class ResultMessage(dtlvmeta.char):
    _name = 'Result-Message'
    _code = 4

class IPv4_Address(dtlvmeta.ipv4_address):
    _name = 'IPv4-Address'
    _code = 5

class MAC48(dtlvmeta.mac48_address):
    _name = 'MAC48-Address'
    _code = 6

class IpPort(dtlvmeta.uint16):
    _name = 'IP-Port'
    _code = 7

class ResultExtCode(dtlvmeta.uint8):
    _name = 'Result-Ext-Code'
    _code = 8

class EventTimestamp(dtlvmeta.date_time):
    _name = 'Event-Timestamp'
    _code = 9

class ServiceMessage(dtlvmeta.objectAVP):
    _name = 'Service-Message'
    _code = 10

class ServiceMessageType(dtlvmeta.uint16):
    _name = 'Service-Message-Type'
    _code = 11

class ServiceConfiguration(dtlvmeta.objectAVP):
    _name = 'Service-Configuration'
    _code = 12

class HostName(dtlvmeta.char):
    _name = 'Host-Name'
    _code = 13

class TimeZone(dtlvmeta.time_zone):
    _name = 'Time-Zone'
    _code = 14

class ServiceName(dtlvmeta.char):
    _name = 'Service-Name'
    _code = 15

class PerepherialId(dtlvmeta.uint8):
    _name = 'Perepherial-GPIO-Id'
    _code = 16

class UpdateTimestamp(dtlvmeta.date_time):
    _name = 'Update-Timestamp'
    _code = 17

class ObjectSize(dtlvmeta.uint16):
    _name = 'Object-Size'
    _code = 18

class MilticastSignal(dtlvmeta.uint8):
    _name = 'Milticast-Signal'
    _code = 19

class SystemDescription(dtlvmeta.char):
    _name = 'System-Description'
    _code = 20
