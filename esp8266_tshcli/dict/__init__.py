from ..dtlv import dtlvmeta

from . import common
from . import service
from . import udpctl
from . import espadmin
from . import ntp
from . import syslog
from . import gpioctl
from . import dht
from . import sched
from . import lsh

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
