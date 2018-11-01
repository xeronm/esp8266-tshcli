#!/usr/bin/python
# -*- coding: utf-8 -*-

import dtlvmeta

import _common as common
import _service as service
import _udpctl as udpctl
import _espadmin as espadmin
import _ntp as ntp
import _syslog as syslog
import _gpioctl as gpioctl
import _dht as dht
import _sched as sched
import _lsh as lsh

dtlvmeta.avpIndex.addModule(common, "common")
dtlvmeta.avpIndex.addModule(service, "service")
dtlvmeta.avpIndex.addModule(udpctl, "uctl")
dtlvmeta.avpIndex.addModule(espadmin, "esp")
dtlvmeta.avpIndex.addModule(ntp, "ntp")
dtlvmeta.avpIndex.addModule(syslog, "syslog")
dtlvmeta.avpIndex.addModule(gpioctl, "gpio")
dtlvmeta.avpIndex.addModule(dht, "dht")
dtlvmeta.avpIndex.addModule(sched, "sched")
dtlvmeta.avpIndex.addModule(lsh, "lsh")
