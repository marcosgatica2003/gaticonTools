#!/bin/bash
region=$(slurp)
dir="$HOME/Imágenes"
mkdir -p "$dir"
filename="screenshot_$(date +%Y-%m-%d_%H-%M-%S).png"
grim -g "$region" "$dir/$filename"
cat "$dir/$filename" | wl-copy
