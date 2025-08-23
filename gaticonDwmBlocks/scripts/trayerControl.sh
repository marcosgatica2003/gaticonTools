#!/bin/sh
if pgrep -x trayer >/dev/null; then
    pkill -x trayer
else
    trayer --edge bottom --align center --widthtype request --SetDockType true --SetPartialStrut true --expand true --transparent true --alpha 0 --tint 0x282828 --height 25 --monitor primary &
fi
