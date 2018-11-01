#!/usr/bin/python
# -*- coding: utf-8 -*-

import dtlvmeta

namespace_id = 2

class Message:
    QUERY = 11

class NS_Syslog(dtlvmeta.namespace):
    _name = 'Syslog'
    _namespace_id = namespace_id

class LogEntry(dtlvmeta.objectAVP):
    _name = 'Log-Entry'
    _code = 101
    _namespace = NS_Syslog

class LogSeverity(dtlvmeta.uint8):
    _name = 'Entry-Severity'
    _code = 102
    _namespace = NS_Syslog

class LogMessage(dtlvmeta.char):
    _name = 'Entry-Message'
    _code = 103
    _namespace = NS_Syslog

class LogTimestamp(dtlvmeta.date_time):
    _name = 'Entry-Timestamp'
    _code = 104
    _namespace = NS_Syslog

class LogRecordNumber(dtlvmeta.uint16):
    _name = 'Entry-Record-Number'
    _code = 105
    _namespace = NS_Syslog

