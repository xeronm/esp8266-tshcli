#!/usr/bin/python
# -*- coding: utf-8 -*-

import dtlvmeta

namespace_id = 4

class NS_UdpControl(dtlvmeta.namespace):
    _name = 'UDP-Control'
    _namespace_id = namespace_id

class ProtocolVersion(dtlvmeta.uint16):
    _name = 'Protocol-Version'
    _code = 100
    _namespace = NS_UdpControl

class NotificationAddr(dtlvmeta.objectAVP):
    _name = 'Notification-Address'
    _code = 101
    _namespace = NS_UdpControl

class IdleTimeout(dtlvmeta.uint16):
    _name = 'Idle-Timeout'
    _code = 102
    _namespace = NS_UdpControl

class AuthTimeout(dtlvmeta.uint16):
    _name = 'Auth-Timeout'
    _code = 103
    _namespace = NS_UdpControl

class RecycleTimeout(dtlvmeta.uint16):
    _name = 'Recycle-Timeout'
    _code = 104
    _namespace = NS_UdpControl

class Secret(dtlvmeta.octets):
    _name = 'Secret'
    _code = 105
    _namespace = NS_UdpControl

class ClientsLimit(dtlvmeta.uint8):
    _name = 'Clients-Limit'
    _code = 106
    _namespace = NS_UdpControl

class Client(dtlvmeta.objectAVP):
    _name = 'Client'
    _code = 107
    _namespace = NS_UdpControl

class ClientState(dtlvmeta.uint8):
    _name = 'Client-State'
    _code = 108
    _namespace = NS_UdpControl
    # ENUM
    STATE_NONE = 0
    STATE_FAIL = 1
    STATE_TIMEOUT = 2
    STATE_AUTH = 3
    STATE_OPEN = 4

class ClientFirstTime(dtlvmeta.date_time):
    _name = 'Client-First-Time'
    _code = 109
    _namespace = NS_UdpControl

class ClientLastTime(dtlvmeta.date_time):
    _name = 'Client-Last-Time'
    _code = 110
    _namespace = NS_UdpControl

class SurveillanceTimeout(dtlvmeta.uint8):
    _name = 'Surveillance-Timeout'
    _code = 111
    _namespace = NS_UdpControl

