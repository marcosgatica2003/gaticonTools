#!/bin/bash

YELLOW='\e[33m'
ORANGE='\e[38;5;208m'
RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
RESET='\e[0m'

function info()    { echo -e "${BLUE}[*] $1${RESET}"; }
function ok()      { echo -e "${GREEN}[✓] $1${RESET}"; }
function warn()    { echo -e "${ORANGE}[!] $1${RESET}"; }
function error()   { echo -e "${RED}[✗] $1${RESET}"; }

function instalar {
    cat /home/marcosgatica/Repositorios/gaticonTools/capturadorDePantallas/gaticonCaptureX11.sh > /usr/local/bin/gaticonCaptureX11
    $PRIV chmod +x /usr/local/bin/gaticonCaptureX11
    ok "Script copiado a /usr/local/bin"
}

if [[ "$1" == "--help" ]]; then
    echo -e "Script para hacer una captura de pantalla. \n"
    echo -e "Las capturas se guardan en el /tmp según fecha y hora, y se copia al portapapeles al momento de capturar."
    echo "Autor: Marcos Raúl Gatica (saludos a LOLON y LULUN)"
    exit 0
fi

if [[ "$1" == "--install" ]]; then
    if [ $(id -u) -ne 0 ]; then 
        echo "Sos un boludo! mete superusuario nomás."
        exit 0
    fi
    instalar
    exit 0
fi

directorio=/tmp
nombreArchivo="captura_$(date +'%Y-%m-%d_%H-%M-%S').png"
nombreRutaGuardado="$directorio/$nombreArchivo"
export nombreRutaGuardado

maim -s --quality 10 | tee >(xclip -selection clipboard -t image/png) > "$nombreRutaGuardado"

notify-send "Captura guardada!" "$nombreArchivo"
