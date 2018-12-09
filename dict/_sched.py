#!/usr/bin/python
# -*- coding: utf-8 -*-

import dtlvmeta

namespace_id = 8

class Message:
    ADD = 10
    REMOVE = 11
    RUN = 12
    SOURCE = 13
    LIST = 14

class NS_Sched(dtlvmeta.namespace):
    _name = 'Scheduler'
    _namespace_id = namespace_id

class SchedEntry(dtlvmeta.objectAVP):
    _name = 'Scheduler-Entry'
    _code = 100
    _namespace = NS_Sched

class EntryName(dtlvmeta.char):
    _name = 'Entry-Name'
    _code = 101
    _namespace = NS_Sched

class EntryState(dtlvmeta.uint8):
    _name = 'Entry-State'
    _code = 102
    _namespace = NS_Sched

class ScheduleString(dtlvmeta.char):
    _name = 'Schedule-String'
    _code = 103
    _namespace = NS_Sched

class StatementName(dtlvmeta.char):
    _name = 'Statement-Name'
    _code = 104
    _namespace = NS_Sched

class StatementArgs(dtlvmeta.objectAVP):
    _name = 'Statement-Args'
    _code = 105
    _namespace = NS_Sched

class LastRunTime(dtlvmeta.date_time):
    _name = 'Last-Run-Time'
    _code = 106
    _namespace = NS_Sched

class NextRunTime(dtlvmeta.date_time):
    _name = 'Next-Run-Time'
    _code = 107
    _namespace = NS_Sched

class RunCount(dtlvmeta.uint16):
    _name = 'Run-Count'
    _code = 108
    _namespace = NS_Sched

class FailCount(dtlvmeta.uint16):
    _name = 'Fail-Count'
    _code = 109
    _namespace = NS_Sched

class Persistent(dtlvmeta.uint8):
    _name = 'Persistent-Flag'
    _code = 110
    _namespace = NS_Sched

class StatementSource(dtlvmeta.objectAVP):
    _name = 'Statement-Source'
    _code = 111
    _namespace = NS_Sched
