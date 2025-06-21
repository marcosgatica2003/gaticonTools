#!/bin/bash

directorio=/tmp
nombreArchivo="captura_$(date +'%Y-%m-%d_%H-%M-%S').png"
nombreRutaGuardado="$directorio/$nombreArchivo"
export nombreRutaGuardado

maim -s --quality 10 | tee >(xclip -selection clipboard -t image/png) > "$nombreRutaGuardado"
