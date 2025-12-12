#!/usr/bin/env python3
import time
import sys 
import os

TEMP_SENSOR = "/run/hwmon-k10temp/temp1_input"
PWM_PATHS = ["/run/hwmon-dell/pwm1", "/run/hwmon-dell/pwm2"]

def readTemp():
    with open(TEMP_SENSOR) as f:
        raw = f.read().strip()
    return int(raw) / 1000.0

def calcPwm(temp, tMin, tMax):
    if temp <= tMin:
        return 0
    if temp >= tMax:
        return 255

    ratio = (temp - tMin) / (tMax - tMin)
    return int(ratio * 255)

def writePwm(value):
    for path in PWM_PATHS:
        try:
            with open(path, "w") as f:
                f.write(str(value))
        except Exception as e:
            print(f"[Error] Escribiendo en {path}: {e}")

def main():
    if len(sys.argv) != 3
        print("Uso: $ ./gaticonFancontrol.py <tempMin> <tempMax>")
        print("Ejemplo: $ ./gaticonFancontrol.py 10 60")
        sys.exit(1)

    tMin = float(sys.argv[1])
    tMax = float(sys.argv[2])

    print(f"[gaticonFancontrol] Controlando ventiladores...")
    print(f"  • Tmin = {t_min}°C -> PWM=0")
    print(f"  • Tmax = {t_max}°C -> PWM=255")

    while True:
        temp = readTemp()
        pwm = calcPwm(temp, Tmin, Tmax)
        writePwm(pwm)

        print(f"T={temp:5.1f}ºC -> PWM={pwm}", end="\r", flush=True)
        time.sleep(0.5)

if __name__ = "__main__":
    main()
