#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ESP8266 Things Shell FAN Control Unit Example
# Copyright (c) 2018 Denis Muratov <xeronm@gmail.com>.
# https://dtec.pro/gitbucket/git/esp8266/esp8266-tsh.git
#
# This file is part of ESP8266 Things Shell Command Line Utility.
#
# ESP8266 Things Shell FAN Control Unit Example is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ESP8266 Things Shell FAN Control Unit Example is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ESP8266 Things Shell FAN Control Unit Example.  If not, see <https://www.gnu.org/licenses/>.
#

import argparse
import os
import time
from proto import *
from dtlv import *
import json
import dtlvmeta

DESCRIPTION = "esp8266 Things Shell: FAN Control Unit Measurements"
FAN_PORT_ID = 0

def parseArgupments():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-p", dest="port", type=int, help="target port", default=3901)
    parser.add_argument("-s", dest="secret", type=str, help="authentication secret", required=True)
    parser.add_argument("-H", dest="host", type=str, help="target host", required=True)

    args = parser.parse_args()
    return args

def check_response(packet):
    if not packet:
        print('no response')
        return False
    res_data = packet.avplist.as_json_serializable()
    if res_data.get('common.Result-Code') != 1:
        print('%s:\n%s' % (message, json.dumps(res_data, indent=4, separators=(',', ': '))) )
        return False
    return res_data

def main():
    output = {}
    args = parseArgupments()
    uc = UdpControlClient(port=args.port, host=args.host, secret=args.secret)     
    if not check_response (uc.auth()):
        exit(-1)

    pinfo = check_response (uc.srvmsg( {
            'esp:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO,
                'esp.System': {}
            }
        }, espadmin.namespace_id ))

    psysinfo = pinfo['esp:common.Service-Message']['esp.System']
    output['common.System-Uptime'] = pinfo['esp:common.Service-Message']['common.System-Uptime']
    output['esp.Heap-Free-Size'] = psysinfo['esp.Heap-Free-Size']
    output['common.Host-Name'] = pinfo['esp:common.Service-Message']['common.Host-Name']

    pdht = check_response (uc.srvmsg( {
            'dht:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, dht.namespace_id ))

    pdhtlast = pdht['dht:common.Service-Message'].get('dht.Stat-Last')
    pdhtavg = pdht['dht:common.Service-Message'].get('dht.Stat-Average')
    if pdhtlast:
        output['dht.Humidity.last'] = pdhtlast.get('dht.Humidity')
        output['dht.Temperature.last'] = pdhtlast.get('dht.Temperature')
        output['dht.DHT-Result-Code'] = pdhtlast.get('dht.DHT-Result-Code')
    if pdhtavg:
        output['dht.Humidity.avg'] = pdhtavg.get('dht.Humidity')
        output['dht.Temperature.avg'] = pdhtavg.get('dht.Temperature')

    pgpio = check_response (uc.srvmsg( {
            'gpio:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, gpioctl.namespace_id ))

    for gpioinfo in pgpio['gpio:common.Service-Message']['gpio.GPIO-Port']:
        if gpioinfo['common.Perepherial-GPIO-Id'] == FAN_PORT_ID:
            output['fan.Port-Value'] = gpioinfo['gpio.GPIO-Port-Value']

    print(json.dumps(output, sort_keys=True, indent=4, separators=(',', ': ')))

main()