#!/usr/bin/python
# -*- coding: utf-8 -*-

import dtlvmeta

namespace_id = 5

class Message:
    STMT_ADD = 10
    STMT_REMOVE = 11
    STMT_RUN = 12
    STMT_DUMP = 13


class NS_Lsh(dtlvmeta.namespace):
    _name = 'Lsh'
    _namespace_id = namespace_id

class ShStatement(dtlvmeta.objectAVP):
    _name = 'SH-Statement'
    _code = 100
    _namespace = NS_Lsh

class ObjectSize(dtlvmeta.uint16):
    _name = 'Object-Size'
    _code = 101
    _namespace = NS_Lsh

class StatementName(dtlvmeta.char):
    _name = 'Statement-Name'
    _code = 102
    _namespace = NS_Lsh

class StatementText(dtlvmeta.char):
    _name = 'Statement-Text'
    _code = 103
    _namespace = NS_Lsh

class StatementCode(dtlvmeta.char):
    _name = 'Statement-Code'
    _code = 104
    _namespace = NS_Lsh

class StatementParseTime(dtlvmeta.date_time):
    _name = 'Statement-Parse-Time'
    _code = 105
    _namespace = NS_Lsh

class StatementArguments(dtlvmeta.objectAVP):
    _name = 'Statement-Arguments'
    _code = 106
    _namespace = NS_Lsh

