#!/bin/bash

function imprimirMensaje {
    echo "------------------------------"
	echo "|    Sistema actualizado!    |"
    echo "------------------------------"

}

if [[ "$1" == "--help" ]]; then
    echo -e "Script para actualizar el sistema operativo GNU/Linux. Simplemente ejecútelo sin argumentos.\n"
    echo -e "Sistemas soportados:\n \t - Debian y derivados. \n \t - Arch Linux y derivados. \n"
    echo "Autor: Marcos Raúl Gatica (saludos a LOLON y LULUN)"
    exit 0
fi


if [ -f /etc/debian_version ]; then
	sudo apt update
	sudo apt full-upgrade --autoremove
	imprimirMensaje
elif [ -f /etc/arch-release ]; then
	sudo pacman -Syyuu
	yay --aur -Syyuu
	imprimirMensaje
else
	echo "Sistema no soportado"
	exit 1
fi
