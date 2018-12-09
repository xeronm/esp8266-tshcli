#!/bin/bash
TSHCTL=/etc/telegraf/telegraf.d/tshcli
export PYTHONPATH=$PYTHONPATH:$TSHCTL

python $TSHCTL/exmaples/fcu.py -H 192.168.5.64 -s 18fe34fca540
