#!/usr/bin/env python3
import socket
import subprocess
import os

def isInterfaceUp(interface):
    try:
        with open(f"/sys/class/net/{interface}/operstate", "r") as f:
            return f.read().strip() == "up"
    except:
            return False

def getWifiSSID(interface):
    try:
        output = subprocess.check_output(["connmanctl", "services"], universal_newlines=True)
        for line in output.strip().splitlines():
            if line.strip().startswith("*"):
                parts = line.strip().split()
                for i, part in enumerate(parts):
                    if part.startswith("wifi_"):
                        ssid_parts = parts[1:i]
                        return " ".join(ssid_parts)
        return "N/A"
    except:
        return "N/A"
def getIPAddress(interface):
    try:
        output = subprocess.check_output(["ip", "-4", "addr", "show", interface,], universal_newlines=True)
        for line in output.split("\n"):
            if "inet " in line:
                return line.split()[1].split("/")[0]
        return "N/A"
    except:
        return "N/A"

def main():

    interfaces = ["wlan0", "wlp4s0", "enp3s0"]

    foundConnection = False
    netInfo = ""

    for interface in interfaces:
        if isInterfaceUp(interface):
            ip = getIPAddress(interface)

            if ip != "N/A":
                if interface.startswith("wl"):
                    ssid = getWifiSSID(interface)
                    if ssid and ssid != "N/A":
                        netInfo = f"^c#222222^^b#679B69^    {ssid}: {ip} ^d^"
                    else:
                        netInfo = f"^c#222222^^b#679B69^    : {ip} ^d^"
                else:
                    netInfo = f"^c#222222^^b#679B69^   : {ip} ^d^"

                foundConnection = True
                break
    if foundConnection:
        print(netInfo)

if __name__ == "__main__":
    main()
