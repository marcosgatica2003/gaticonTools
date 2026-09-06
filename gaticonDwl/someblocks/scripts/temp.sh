#!/bin/bash
TEMP="$(/bin/sensors | /usr/bin/grep Tctl | /usr/bin/awk '{print$2}')"
echo " $TEMP "
