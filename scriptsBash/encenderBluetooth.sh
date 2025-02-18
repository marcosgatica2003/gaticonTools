#!/bin/bash

echo "Encendiendo el servicio de Bluetooth..."
sudo systemctl unmask bluetooth.service
sudo systemctl start bluetooth.service
echo "Servicio de Bluetooth encendido."

