#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# ESP8266 Things Shell Command Line Utility
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

from __future__ import print_function
import argparse
from collections import OrderedDict
from operator import itemgetter
import logging 
import os
import time
logging.basicConfig(format='[%(asctime)s] %(levelname) 9s %(module)s: %(message)s', level=logging.WARNING)

from proto import *
from dtlv import *
import json
import socket
import dtlvmeta

DESCRIPTION = "esp8266 Things Shell UDP control utility"

class ExitCodes:
    AUTH_ERROR = 1
    COMMAND_ERROR = 2
    TIMEOUT = 3
    INVALID_USAGE = -1

class Control:

    def __init__(self, args):
        self.args = args
        self.uc = UdpControlClient(port=args.port, host=args.host, secret=args.secret)

    def check_response(self, packet, message):
        if not packet:
            print('%s: no response' % message)
            return False
        res_data = packet.avplist.as_json_serializable()
        if res_data.get('common.Result-Code') != 1:
            print('%s:\n%s' % (message, json.dumps(res_data, indent=4, separators=(',', ': '))) )
            return False
        return res_data


    def auth(self):
        res = self.uc.auth()
        if not self.check_response(res, 'Authentication Error'):
            exit( ExitCodes.AUTH_ERROR )

    def cmd_udpctl(self):
        """UDP control service commands"""
        pass

    def cmd_firmware(self):
        """firmware commands"""
        pass

    def cmd_service(self):
        """service manager commands"""
        pass

    def cmd_system(self):
        """common system commands"""
        pass

    def cmd_dht(self):
        """DHTxx (humidity/temperature sensor) service commands"""
        pass

    def cmd_gpio(self):
        """GPIO perepherial service commands"""
        pass

    def cmd_sched(self):
        """scheduler commands"""
        pass

    def cmd_lsh(self):
        """light-weight shell commands"""
        pass

    def cmd_lsh_info(self):
        """query scheduler information"""
        return self.uc.srvmsg( {
            'lsh:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, lsh.namespace_id )

    def cmd_lsh_add(self):
        """add lsh named statement (required: -m)

MESSAGE example:
  {
    "lsh.Statement-Name": "stmt_action01",
    "lsh.Statement-Text": "## last_sdt; # sdt := sysdate(); print(last_sdt, sdt - last_sdt); (sdt % 2 = 0) ? print(0) : print(1); last_sdt := sdt;"
  }
"""
        msg = OrderedDict([ ('common.Service-Message-Type', lsh.Message.STMT_ADD) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'lsh:common.Service-Message': msg
        }, lsh.namespace_id )

    def cmd_lsh_remove(self):
        """delete lsh statement (required: -m)

MESSAGE example:
  { "lsh.Statement-Name": "stmt_action01" }
"""
        msg = OrderedDict([ ('common.Service-Message-Type', lsh.Message.STMT_REMOVE) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'lsh:common.Service-Message': msg
        }, lsh.namespace_id )

    def cmd_lsh_run(self):
        """run lsh statement (required: -m)

MESSAGE example:
  { "lsh.Statement-Name": "stmt_action01" }
"""
        msg = OrderedDict([ ('common.Service-Message-Type', lsh.Message.STMT_RUN) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'lsh:common.Service-Message': msg
        }, lsh.namespace_id )

    def cmd_lsh_dump(self):
        """dump bytecode for lsh statement (required: -m)

MESSAGE example:
  { "lsh.Statement-Name": "stmt_action01" }
"""
        msg = OrderedDict([ ('common.Service-Message-Type', lsh.Message.STMT_DUMP) ])
        msg.update(self.args.message)
        res = self.uc.srvmsg( {
            'lsh:common.Service-Message': msg
        }, lsh.namespace_id )

        res_data = res.avplist.as_json_serializable()
        service_msg = res_data.get('lsh:common.Service-Message')
        if service_msg and service_msg.get('lsh.Statement-Code'):
            print('bytecode:\n%s\n\n' % service_msg['lsh.Statement-Code'])

        return res


    def cmd_sched_info(self):
        """query scheduler information"""
        return self.uc.srvmsg( {
            'sched:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, sched.namespace_id )

    def cmd_sched_add(self):
        """add scheduler entry (required: -m)

MESSAGE example:
  {
    "sched.Entry-Name": "myentry1",
    "sched.Schedule-String": "0 0,12,24,36,48 * * *",
    "sched.Statement-Name": "stmt_action01",
    "sched.Statement-Args": {}
  }

  Schedule-String format:
      0-3    - minute parts
      0-59   - minutes
      0-24   - hours
      1-31   - days of month
      0-6    - days of week
"""
        msg = OrderedDict([ ('common.Service-Message-Type', sched.Message.ADD) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'sched:common.Service-Message': msg
        }, sched.namespace_id )

    def cmd_sched_remove(self):
        """remove scheduler entry (required: -m)

MESSAGE example:
  { "sched.Entry-Name": "myentry1" }
"""
        msg = OrderedDict([ ('common.Service-Message-Type', sched.Message.REMOVE) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'sched:common.Service-Message': msg
        }, sched.namespace_id )

    def cmd_sched_run(self):
        """run scheduler entry (required: -m)

MESSAGE example:
  { "sched.Entry-Name": "myentry1" }
"""
        msg = OrderedDict([ ('common.Service-Message-Type', sched.Message.RUN) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'sched:common.Service-Message': msg
        }, sched.namespace_id )

    def cmd_udpctl_info(self):
        """query udpctl information"""
        return self.uc.srvmsg( {
            'uctl:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, udpctl.namespace_id )

    def cmd_firmware_verify(self):
        """verify firmware digest"""
        return self.uc.srvmsg( {
            'esp:common.Service-Message': {
                'common.Service-Message-Type': espadmin.Message.FW_VERIFY
            }
        }, espadmin.namespace_id )

    def cmd_firmware_info(self):
        """query current firmware info"""
        return self.uc.srvmsg( {
            'esp:common.Service-Message': OrderedDict([
                ('common.Service-Message-Type', common.Message.INFO),
                ('esp.Firmware', {}),
            ])
        }, espadmin.namespace_id )

    def cmd_firmware_upgrade(self):
        """firmware upgarde (required: -f)"""

        # query current bin addr
        res = self.uc.srvmsg( {
            'esp:common.Service-Message': OrderedDict([
                ('common.Service-Message-Type', common.Message.INFO),
                ('esp.Firmware', {}),
            ])
        }, espadmin.namespace_id )
        if not self.check_response(res, 'Command Error: Query current Firmware Info'):
            exit( ExitCodes.COMMAND_ERROR )

        res_data = res.avplist.as_json_serializable()
        service_msg = res_data.get('esp:common.Service-Message')
        if not service_msg or not service_msg.get('esp.Firmware'):
            print("Command Error: Failed to get current firmware info")
            exit( ExitCodes.COMMAND_ERROR )

        size_map = service_msg['esp.Firmware']['esp.FW-Size-Map']
        fw_address = service_msg['esp.Firmware']['esp.FW-Address']

        print("""
Running Firmware:
    Product: %s
    Version: %s
    Address: %s
    BinDate: %s
""" % ( service_msg['common.Application-Product'], service_msg['common.Application-Version'], fw_address, service_msg['esp.Firmware'].get('esp.FW-Bin-Date')))

        bundle_info = None
        with open(self.args.firmware, 'r') as f:
            bundle_info = json.loads(f.read())

        firmware_info = None
        for item in bundle_info:
            if item['fw_addr'] != fw_address:
                firmware_info = item

        if not firmware_info:
            print("Command Error: Firmware not compartible, current spi:%d, addr:%s" % (size_map, fw_address))
            exit( ExitCodes.COMMAND_ERROR )

        firmware_file = os.path.join(os.path.split(self.args.firmware)[0], firmware_info['file_mame'])
        print("""Uploading Firmware: %s
    Product: %s
    Version: %s
    Address: %s
    BinDate: %s
""" % (firmware_file, firmware_info['product'], firmware_info['version'], firmware_info['fw_addr'], time.strftime(dtlvmeta.c_time_format, time.localtime(firmware_info['bin_date'])) ))

        res = self.uc.srvmsg( {
            'esp:common.Service-Message': OrderedDict([
                ('common.Service-Message-Type', espadmin.Message.FW_OTA_INIT),
                ('esp.FW-Init-Digest', firmware_info['initial_digest']),
                ('esp.FW-Info', firmware_info['fw_info']),
            ])
        }, espadmin.namespace_id )
        if not self.check_response(res, 'Command Error: Initialize Firmware Upgrade'):
            exit( ExitCodes.COMMAND_ERROR )

        print('Upgrade initialized, uploading...')

        data = None
        with open(firmware_file, 'r') as f:
            data = f.read()

        binlen = len(data)
        last_pct = 0
        print('Uploading ...', end=' ')
        sys.stdout.flush()
        for i in range(0, binlen, 1024):
            data_chunk = data[i:i+1024]
            res = self.uc.srvmsg( {
                'esp:common.Service-Message': OrderedDict([
                    ('common.Service-Message-Type', espadmin.Message.FW_OTA_UPLOAD),
                    ('esp.OTA-Bin-Data', binascii.hexlify(data_chunk)),
                ])
            }, espadmin.namespace_id )
            if not self.check_response(res, 'Command Error: Firmware upload'):
                exit( ExitCodes.COMMAND_ERROR )

            pos_pct = (i + len(data_chunk))*100/binlen
            print('\rUploading %d%% ...' % (pos_pct), end=' ')
            sys.stdout.flush()
        print('Done.')

        res = self.uc.srvmsg( {
            'esp:common.Service-Message': OrderedDict([
                ('common.Service-Message-Type', espadmin.Message.FW_OTA_DONE),
            ])
        }, espadmin.namespace_id )
        if not self.check_response(res, 'Command Error: Firmware upgrade done'):
            exit( ExitCodes.COMMAND_ERROR )

        print('Upgrade Done. Waiting system up...')
        time.sleep(7)

        print('Verifying...')
        self.auth()
        res = self.uc.srvmsg( {
            'esp:common.Service-Message': OrderedDict([
                ('common.Service-Message-Type', common.Message.INFO),
                ('esp.Firmware', {}),
            ])
        }, espadmin.namespace_id )
        if not self.check_response(res, 'Command Error: Query ugraded Firmware Info'):
            exit( ExitCodes.COMMAND_ERROR )

        res_data = res.avplist.as_json_serializable()
        service_msg = res_data.get('esp:common.Service-Message')
        if not service_msg or not service_msg.get('esp.Firmware'):
            print("Command Error: Failed to get upgraded firmware info")
            exit( ExitCodes.COMMAND_ERROR )

        fw_address = service_msg['esp.Firmware']['esp.FW-Address']
        print("""
Result Firmware:
    Product: %s
    Version: %s
    Address: %s
    BinDate: %s
""" % ( service_msg['common.Application-Product'], service_msg['common.Application-Version'], fw_address, service_msg['esp.Firmware'].get('esp.FW-Bin-Date')))

        return res

    def cmd_system_restart(self):
        """restart system"""
        return self.uc.srvmsg( {
            'esp:common.Service-Message': {
            'common.Service-Message-Type': espadmin.Message.RESTART
            }
        }, espadmin.namespace_id )

    def cmd_system_truncfdb(self):
        """truncate Flash-DB (will restart system)"""
        return self.uc.srvmsg( {
            'esp:common.Service-Message': {
            'common.Service-Message-Type': espadmin.Message.FDB_TRUNC
            }
        }, espadmin.namespace_id )

    def cmd_service_info(self):
        """query services information"""
        return self.uc.srvmsg( {
            'service:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, service.namespace_id )

    def cmd_service_control(self):
        """services control operations (required: -m)

MESSAGE example:
  { "service.Service": [ 
      {
        "service.Service-Id": 8, 
        "service.Service-Enabled": 1
      } 
    ] 
  }"""
        msg = OrderedDict([ ('common.Service-Message-Type', service.Message.CONTROL) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'service:common.Service-Message': msg
        }, service.namespace_id )

    def cmd_service_getconfig(self):
        """services stored configuration get (required: -m)

MESSAGE example:
  { "service.Service": [ 
      { "service.Service-Id": 8 } 
    ] 
  }"""
        msg = OrderedDict([ ('common.Service-Message-Type', service.Message.CONFIG_GET) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'service:common.Service-Message': msg
        }, service.namespace_id )

    def cmd_system_info(self):
        """query system information (optional: -m)

MESSAGE example:
  {
    "esp.System": {},
    "esp.Firmware": {},
    "esp.Memory-DB": {},
    "esp.Flash-DB": {},
    "esp.Wireless": {},
  }

  System   - system inforantion
  Firmware - firmware inforantion
  MemoryDB - in-memory DB information and statistics
  FlashDB  - flash DB information and statistics
  Wireless - wi-fi parameters and status
"""
        msg = OrderedDict([ ('common.Service-Message-Type', common.Message.INFO) ])
        if self.args.message:
            msg.update(self.args.message)
        else:
            msg.update({ "esp.System": {}, "esp.Firmware": {} })
        return self.uc.srvmsg( {
            'esp:common.Service-Message': msg
        }, espadmin.namespace_id )

    def cmd_ntp_info(self):
        """query ntp service information"""
        return self.uc.srvmsg( {
            'ntp:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, ntp.namespace_id )

    def cmd_syslog_query(self):
        """query syslog messages"""
        return self.uc.srvmsg( {
            'syslog:common.Service-Message': {
                'common.Service-Message-Type': syslog.Message.QUERY
            }
        }, syslog.namespace_id )

    def cmd_gpio_info(self):
        """query GPIO service information"""
        return self.uc.srvmsg( {
            'gpio:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, gpioctl.namespace_id )

    def cmd_gpio_set(self):
        """set gpio output (required: -m)

MESSAGE example:
  {
    "common.Perepherial-GPIO-Id": "4",
    "gpio.GPIO-Port-Value": "1",
    "gpio.GPIO-Port-Pulse-us": "100",
    "gpio.GPIO-Function-Set": "0",
    "gpio.GPIO-Port-Pullup": "1"
  }

  GPIO-Id  - GPIO pin identifier
  Value    - output value (0|1|0xFF), 0xFF - means disable output
  Pulse-us - pulse microseconds (optional), switch output to negative Value after pulse microseconds
  Function-Set - function (optional), select function for pin 
  Pullup   - pullup state (0|1|optional), disable/enable pullup for pin
"""
        msg = OrderedDict([ ('common.Service-Message-Type', gpioctl.Message.GPIO_SET) ])
        msg.update(self.args.message)
        return self.uc.srvmsg( {
            'gpio:common.Service-Message': msg
        }, gpioctl.namespace_id )

    def cmd_dht_info(self):
        """query DHT service information"""
        return self.uc.srvmsg( {
            'dht:common.Service-Message': {
                'common.Service-Message-Type': common.Message.INFO
            }
        }, dht.namespace_id )

    def execute(self, args):
        cmd = '_'.join(['cmd'] + args.command)
        if not hasattr(self, cmd):
            print('invalid commands: %s' % ' '.join(args.command))
            return False

        fcnt = 0
        for key, value in self.__class__.__dict__.items():
            if key.startswith(cmd):
                fcnt += 1
        if fcnt > 1:
            Control.command_help(args.command)
            exit(ExitCodes.INVALID_USAGE)

        func = getattr(self, cmd)        
        res = func()
        if not self.check_response(res, 'Command Error'):
            exit( ExitCodes.COMMAND_ERROR )
        else:
            res_data = res.avplist.as_json_serializable()
            print(json.dumps(res_data, indent=4, separators=(',', ': ')))


    @classmethod
    def command_help(cls, path):
        """ path = ['firmware', ''] """
        items = []
        path_str = '_'.join(['cmd'] + path) + '_'
        root_help = None
        for key, value in cls.__dict__.items():
            if key == path_str[:-1]:
                root_help = value.__doc__
                continue
            if not key.startswith(path_str):
                continue
            key = key[len(path_str):]
            if key.find('_') != -1: 
                continue
            items.append((key, value.__doc__.split('\n')[0]))

        if root_help:
            print("command usage: %s [command ...]\n\ndescription:\n  %s\n\nsub-commands:" % (' '.join(path), root_help))
        else:
            print("commands:")
        for (key, value) in sorted(items, key=itemgetter(0)) :
            print("  %-14s %s" % (key, value))

def parseArgupments(first_pass=False):
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-p", dest="port", type=int, help="target port", default=3901)
    parser.add_argument("-s", dest="secret", type=str, help="authentication secret", required=not first_pass)
    parser.add_argument("-H", dest="host", type=str, help="target host", required=not first_pass)
    parser.add_argument("-f", dest="firmware", type=str, help="firmware bundle info file")
    parser.add_argument("-m", dest="message", type=str, help="JSON message to send in command")
    parser.add_argument("command", nargs='*', type=str, help="control command (default: help)")

    args = parser.parse_args()

    if args.message:
        args.message = json.loads(args.message)
    else:
        args.message = {}

    return args

def main():
    args = parseArgupments(True)

    if not args.command or args.command[-1] == 'help':
        Control.command_help(args.command[:-1])
        exit(ExitCodes.INVALID_USAGE)

    args = parseArgupments()
    ctl = Control(args)

    try:
        ctl.auth()
        ctl.execute(args)
    except socket.timeout:
        print('Transport Error: socket timeout')
        exit(ExitCodes.TIMEOUT)
     

main()