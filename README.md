esp8266-tshcli
===============
Client utilities for ESP8266 Light-weight Shell [esp8266-tsh]

[esp8266-tsh]: https://github.com/xeronm/esp8266-tsh


### Getting started

Build python package
```sh
$ pip3 install build
$ python3 -m build
```

Install python package
```
$ export PIP_FIND_LINKS=./dist/
$ pip3 install esp8266_tshcli
```

### CLI utility ###

#### Geting help

```sh
$ python3 -m esp8266_tshcli -h
$ python3 -m esp8266_tshcli 
```

#### Query system information

```sh
$ python3 -m esp8266_tshcli -H 192.168.5.64 -s 18fe34fca540 system info
```

```json
{
    "common.Event-Timestamp": "2024.10.27 09:46:28",
    "esp:common.Service-Message": {
        "common.Application-Product": "esp8266 Things Shell (c) 2018 dtec.pro",
        "common.Application-Version": "0.2.2-dev(819)",
        "common.Host-Name": "ESP_FCA540",
        "common.System-Description": "Bathroom FAN#1",
        "common.System-Uptime": 1795,
        "esp.System": {
            "esp.System-SDK-Version": "2.2.0-dev(9422289)",
            "esp.System-Chip-ID": 16557376,
            "esp.System-Flash-ID": 1458400,
            "esp.Heap-Free-Size": 12984,
            "esp.System-Reset-Reason": 6,
            "esp.System-CPU-Frequence": 80,
            "esp.System-Boot-Loader-Version": 7
        },
        "esp.Firmware": {
            "esp.FW-Address": "0x081000",
            "esp.FW-Size-Map": 4,
            "esp.FW-Bin-Size": 339760,
            "esp.FW-Bin-Date": "2019.04.13 19:20:47",
            "esp.FW-User-Data-Address": "0x0fd000",
            "esp.FW-User-Data-Size": 3133440,
            "esp.FW-Release-Date": "2018.12.16 23:43:05",
            "esp.FW-Digest": "316389f388ddd7aafaa238129194eddee03b2870a6f6cdc773b8c4028cc4defa",
            "esp.FW-Init-Digest": "4646303030303030303030303030303030303030303030303030303030304646"
        }
    },
    "common.Result-Code": 1
}
```

#### Query log record
```sh
$ python3 -m esp8266_tshcli -H 192.168.5.64 -s 18fe34fca540 syslog query
```

```json
{
    "common.Event-Timestamp": "2024.10.27 10:08:14",
    "syslog:common.Service-Message": {
        "syslog.Log-Entry": [
            {
                "syslog.Entry-Record-Number": 41,
                "syslog.Log-Severity": 3,
                "syslog.Entry-Timestamp": "2024.10.27 10:01:58",
                "common.Service-Name": "ntp",
                "syslog.Entry-Message": "adjust time failed"
            },
            {
                "syslog.Entry-Record-Number": 40,
                "syslog.Log-Severity": 3,
                "syslog.Entry-Timestamp": "2024.10.27 09:46:48",
                "common.Service-Name": "ntp",
                "syslog.Entry-Message": "adjust time failed"
            },
            {
                "syslog.Entry-Record-Number": 39,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:32:15",
                "common.Service-Name": "lwsh",
                "syslog.Entry-Message": "fan_control out: 4"
            },
            {
                "syslog.Entry-Record-Number": 38,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:32:15",
                "common.Service-Name": "lwsh",
                "syslog.Entry-Message": "load \"fan_control\""
            },
            {
                "syslog.Entry-Record-Number": 37,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:32:03",
                "common.Service-Name": "svcs",
                "syslog.Entry-Message": "broadcast message:36"
            },
            {
                "syslog.Entry-Record-Number": 36,
                "syslog.Log-Severity": 3,
                "syslog.Entry-Timestamp": "2024.10.27 09:32:03",
                "common.Service-Name": "ntp",
                "syslog.Entry-Message": "adjust time from: 1970.01.01 03:15:30+3:00 to:2024.10.27 09:32:04+3:00"
            },
            {
                "syslog.Entry-Record-Number": 35,
                "syslog.Log-Severity": 3,
                "syslog.Entry-Timestamp": "2024.10.27 09:21:33",
                "common.Service-Name": "main",
                "syslog.Entry-Message": "softap timeout"
            },
            {
                "syslog.Entry-Record-Number": 34,
                "syslog.Log-Severity": 3,
                "syslog.Entry-Timestamp": "2024.10.27 09:17:27",
                "common.Service-Name": "ntp",
                "syslog.Entry-Message": "adjust time failed"
            },
            {
                "syslog.Entry-Record-Number": 33,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:37",
                "common.Service-Name": "svcs",
                "syslog.Entry-Message": "broadcast message:34"
            },
            {
                "syslog.Entry-Record-Number": 32,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "udpctl",
                "syslog.Entry-Message": "listen port:3901, secret length:12"
            },
            {
                "syslog.Entry-Record-Number": 31,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "lwsh",
                "syslog.Entry-Message": "fan_force_on out: 1"
            },
            {
                "syslog.Entry-Record-Number": 30,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "lwsh",
                "syslog.Entry-Message": "load \"fan_force_on\""
            },
            {
                "syslog.Entry-Record-Number": 29,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "svcs",
                "syslog.Entry-Message": "broadcast message:32"
            },
            {
                "syslog.Entry-Record-Number": 28,
                "syslog.Log-Severity": 3,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "startup",
                "syslog.Entry-Message": "done, fmem:15320"
            },
            {
                "syslog.Entry-Record-Number": 27,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "main",
                "syslog.Entry-Message": "overflow timer:36 min"
            },
            {
                "syslog.Entry-Record-Number": 26,
                "syslog.Log-Severity": 3,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "svcs",
                "syslog.Entry-Message": "\"dev.dht\" started"
            },
            {
                "syslog.Entry-Record-Number": 25,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "gpioctl",
                "syslog.Entry-Message": "acquire gpio_id:4, addr:6000083c,func:0,pull:1"
            },
            {
                "syslog.Entry-Record-Number": 24,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "dev.dht",
                "syslog.Entry-Message": "gpio:4, timeout:20"
            },
            {
                "syslog.Entry-Record-Number": 23,
                "syslog.Log-Severity": 4,
                "syslog.Entry-Timestamp": "2024.10.27 09:16:33",
                "common.Service-Name": "svcs",
                "syslog.Entry-Message": "\"dev.dht\" [id:21] installing"
            }
        ]
    },
    "common.Result-Code": 1
}
```

#### Collect Measurements

```sh
$ python3 ./example/espfan.py -H 192.168.5.64 -s 18fe34fca540
```

```json
{
    "common.Host-Name": "ESP_FCA540",
    "common.System-Uptime": 2197,
    "dht.DHT-Result-Code": 0,
    "dht.Humidity.avg": 3200,
    "dht.Humidity.last": 3200,
    "dht.Temperature.avg": 2500,
    "dht.Temperature.last": 2500,
    "esp.Heap-Free-Size": 12816,
    "fan.Port-Value": 1
}
```

#### Upgrade firmware

```sh
$ python3 -m esp8266_tshcli -H 192.168.5.64 -s 18fe34fca540 -f ./../tsh/bin/tsh-0.1.0-dev.spi4.info.json firmware upgrade 
```


