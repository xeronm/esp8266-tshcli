#!/usr/bin/python
# -*- coding: utf-8 -*-

import dtlvmeta

namespace_id = 21

class NS_DHT(dtlvmeta.namespace):
    _name = 'DHT'
    _namespace_id = namespace_id

class SensorType(dtlvmeta.uint8):
    _name = 'Sensor-Type'
    _code = 100
    _namespace = NS_DHT

class StatTimeout(dtlvmeta.uint8):
    _name = 'Stat-Timeout'
    _code = 101
    _namespace = NS_DHT

class HistInterval(dtlvmeta.uint8):
    _name = 'Hist-Interval'
    _code = 102
    _namespace = NS_DHT

class EMA_AlphaPct(dtlvmeta.uint8):
    _name = 'EMA-Alpha-Percent'
    _code = 103
    _namespace = NS_DHT

class Humidity(dtlvmeta.uint16):
    _name = 'Humidity'
    _code = 104
    _namespace = NS_DHT

class Temperature(dtlvmeta.uint16):
    _name = 'Temperature'
    _code = 105
    _namespace = NS_DHT

class ResultCode(dtlvmeta.uint8):
    _name = 'DHT-Result-Code'
    _code = 106
    _namespace = NS_DHT

class StatLastTime(dtlvmeta.date_time):
    _name = 'Stat-Last-Time'
    _code = 107
    _namespace = NS_DHT

class StatLast(dtlvmeta.objectAVP):
    _name = 'Stat-Last'
    _code = 108
    _namespace = NS_DHT

class StatAverage(dtlvmeta.objectAVP):
    _name = 'Stat-Average'
    _code = 109
    _namespace = NS_DHT

class EMA_InitCount(dtlvmeta.uint8):
    _name = 'EMA-Initialize-Counter'
    _code = 110
    _namespace = NS_DHT
