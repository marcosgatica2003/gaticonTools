#!/bin/bash

INTERFACE="wlp4s0"

redesDisponibles() {
    clear
    echo "----------------------------------------------"
    echo "              Redes disponibles               "
    echo -e "----------------------------------------------\n"
    iwlist $INTERFACE scan | grep -E "ESSID|Signal"
    sleep 2
    echo "----------------------------------------------"

    echo -e "\t \n Pulse ENTER para continuar."
    read 
}

agregarNuevaRed() {
    read -p "SSID: " SSID
    read -p "Contraseña: " PASSWORD

    if [[ ! -d "/etc/redes" ]]; then
        echo "Directorio redes creado en /etc/redes"
        mkdir -p "/etc/redes"
    fi

    if [ -f "/etc/redes/$SSID.conf" ]; then
        read -p "La red '$SSID' existe, pisar? (1 - Sí / 2 - No): " OPCION

        if [[ "$OPCION" == 2 ]]; then
            echo "No se pisa"
            return 1
        else
            echo "Se pisa"
        fi

    fi
    
    wpa_passphrase "$SSID" "$PASSWORD" > /etc/redes/"$SSID".conf
    echo -e "--- Red $SSID agregada ---\n"
    echo -e "---> Enter para continuar <---"
    read
}

conectarWifi() {
    clear
    systemctl start wpa_supplicant.service
    ip link set "$INTERFACE" up
    
    local redDir="/etc/redes"

    if [[ ! -d "/etc/redes" ]]; then
        echo "Directorio redes creado en /etc/redes"
        mkdir -p "/etc/redes"
    fi


    if [ ! -d "$redDir" ]; then
        echo "No hay redes conocidas."
        return 1
    fi

    for redDir in "$redDir"/*.conf; do
        local SSID=$(basename "$redDir".conf)
        echo "Intentando conectar a la red: $SSID..."
        wpa_supplicant -B -i "$INTERFACE" -c "$redDir" > /dev/null 2>&1
        dhclient "$INTERFACE" > /dev/null 2>&1
        sleep 3

        if ping -q -c 1 -W 3 google.com > /dev/null 2>&1; then
            echo "Red '$SSID' conectada"
            return 0
        else
            echo "No se pudo con $SSID"
            killall wpa_supplicant > /dev/null 2>&1
        fi
    done

    echo "No hay redes conocidas disponibles."
    return 1
}

redesConocidas() {

    local redDir="/etc/redes"
    if [ ! -d "$redDir" ]; then
        echo -e "\t Sin redes, boludo."
        read
    fi
    clear
    echo "----------------------------------------------"
    echo "                Redes Conocidas               "
    echo "----------------------------------------------"
    if [ ! -d "$redDir" ]; then
        echo -e "\t Sin redes, boludo.\n"
        echo -e "\t---> Enter para continuar <---"
        read
    fi

    local REDES=$(ls "$redDir"/*.conf 2>/dev/null)
    if [ -z "$REDES" ]; then
        echo "No hay redes configuradas en $redDir."
        echo -e "---> Enter para continuar <---"
        read 
        return 1
    fi 

    ls "$redDir"/*.conf | xargs -n 1 basename | sed 's/\.conf$//' | nl -w2 -s". " 

    echo -e "----------------------------------------------\n"
    echo "Total: $(ls "$redDir"/*.conf | wc -l) redes."
    echo "----------------------------------------------"
    echo -e "---> Enter para continuar <---"
    read 

}

notMel() {
    clear
    ./notMel.sh
    sleep 1
    echo -e "----------------------------------------------"
    echo -e "                No es mel                     "
    echo -e "----------------------------------------------"
    echo -e "---> Enter para continuar <---"
    read 
}

desconectarWifi() {
    killall wpa_supplicant
    killall dhclient
    echo -e "----------------------------------------------"
    echo    "     Apagando wpa_supplicant y dhclient...    "
    echo -e "----------------------------------------------"
    echo -e "---> Enter para continuar <---"
    read 
}

autor() {
    clear
    echo "----------------------------------------------"
    echo "           Información del programa           "
    echo "----------------------------------------------"
    echo -e "\n"
    echo -e " 1 - Autor: Marcos Raúl Gatica           "
    echo -e " 2 - Última fecha de modificación: 18 - 12 - 2024"
    echo -e " 3 - Versión del programa: 1.0"
    echo -e "\n"
    echo -e "---> Diseñado para Arch Linux y Debian <---"
    echo -e "--- Mel no estuvo aquí ---"
    echo "----------------------------------------------"
    echo -e "---> Enter para continuar <---"
    read 

}

if [[ "$1" == "--conectar" ]]; then
    conectarWifi
    exit 0
fi


while true; do
    clear
    echo "----------------------------------------------"
    echo "                Gestor WiFi                   "
    echo "----------------------------------------------"
    echo -e "\t1. Redes disponibles"
    echo -e "\t2. Agregar nueva red WiFi"
    echo -e "\t3. Conectar el WiFi"
    echo -e "\t4. Ver redes conocidas"
    echo -e "\t5. Es mel? "
    echo -e "\t6. Desconectar"
    echo -e "\t7. Información"
    echo -e "\t8. Salir y guardar"
    echo "----------------------------------------------"
    read -p "Mete una opción: " OPCION

    case $OPCION in
        1) redesDisponibles ;;
        2) agregarNuevaRed ;;
        3) conectarWifi ;;
        4) redesConocidas ;;
        5) notMel ;;
        6) desconectarWifi ;;
        7) autor ;;
        8) echo "Saliendo..."; exit 0 ;;
        *) clear; echo "Opción no válida"; sleep 2 ;;
    esac
done

