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


