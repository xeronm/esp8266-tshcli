esp8266-tshcli
===============
Client utilities for ESP8266 Light-weight Shell [esp8266-tsh]

[esp8266-tsh]: https://github.com/xeronm/esp8266-tsh

### CLI utility ###

```
# help
$ ./tcli.py -h
# list all top-level commands
$ ./tcli.py
# Query system information
$ ./tcli.py -H 192.168.5.64 -s 18fe34fca540 system info
# Upgrade Firmware
$ ./tcli.py -H 192.168.5.64 -s 18fe34fca540 -f ./../tsh/bin/tsh-0.1.0-dev.spi4.info.json firmware upgrade 
```


