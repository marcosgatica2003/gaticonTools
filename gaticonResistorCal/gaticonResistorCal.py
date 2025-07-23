#!/usr/bin/env python3

import sys
import shutil
import os
import argparse

def install():
    source = os.path.relpath(__file__)
    destino = "/usr/local/bin/gaticonResistorCal"

    try:
        shutil.copy(source, destino)
        os.chmod(destino, 0o755)
        print(f"gaticonResistorCal se instaló en '{destino}'")
    except PermissionError:
        print("Imbécil necesitas permisos de los GOD")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def showHelp():
    print("Script para calcular la resistencia de los resistores con colores. Simplemente ejecútelo sin argumentos")
    print("--help -> Muestra esto :v")
    print("--install -> lo instala en /usr/local/bin")
    print("Autor: Marcos Raúl Gatica (saludos a LOLON y LULUN)")
    sys.exit()

bandValues = {
    'negro': 0, 
    'marron': 1, 
    'rojo': 2, 
    'naranja': 3,
    'amarillo': 4,
    'verde': 5,
    'azul': 6,
    'violeta': 7,
    'gris': 8,
    'blanco': 9
}

multipliers = {
    'negro': 1,
    'marron': 10,
    'rojo': 100,
    'naranja': 1_000,
    'amarillo': 10_000,
    'verde': 100_000,
    'azul': 1_000_000,
    'violeta': 10_000_000,
    'gris': 100_000_000,
    'blanco': 1_000_000_000,
    'dorado': 0.1,
    'plateado': 0.01
}

toleranceValues = {
    'marron': '±1%',
    'rojo': '±2%',
    'dorado': '±5%',
    'plateado': '±10%'
}

def formatResistance(ohmValue):
    if ohmValue >= 1_000_000:
        returnValue = f"{ohmValue/1_000_000:.2f} MΩ"

    elif ohmValue >= 1_000:
        returnValue = f"{ohmValue/1_000:.2f} kΩ"

    else:
        returnValue = f"{ohmValue:.2f} Ω"

    return returnValue

def calculateResistance(band1, band2, multiplierColor):
    digits = bandValues[band1] * 10 + bandValues[band2]
    return digits * multipliers[multiplierColor]

def helpBands():
    print("Primera y segunda banda:")
    print("------------------------")
    for color, value in bandValues.items():
        print(f"{color:10} → {value}")

    print("\nTercera banda (multiplicidad):")
    print("------------------------------")
    for color, value in multipliers.items():
        print(f"{color:10} → {value}")

    print("\nCuarta banda (tolerancia):")
    print("--------------------------")
    for color, value in toleranceValues.items():
        print(f"{color:10} → {value}")

def setBandColor(n):
    while True:
        bandX = input(f"Color {n}: ").strip().lower()

        if bandX == 'exit':
            print("chau")
            sys.exit()

        if bandX == 'help':
            helpBands()
            continue

        if bandX == "" and n == 4:
            break

        if bandX not in bandValues and bandX not in multipliers and bandX not in toleranceValues:
            print("Color inválido")
        else:
            break

    return bandX

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--install", action="store_true")
    parser.add_argument("--help", action="store_true")

    args = parser.parse_args()

    if args.help:
        showHelp()
        sys.exit()

    if args.install:
        install()
        sys.exit()

    print("Mete 'exit' para salir pos p hijito.\n")
    while True:
        band1 = setBandColor(1)
        band2 = setBandColor(2)
        band3= setBandColor(3)
        band4= setBandColor(4)

        ohm = calculateResistance(band1, band2, band3)

        result = formatResistance(ohm)
        toler = toleranceValues.get(band4, '')
        print(f"\n→ Resistencia: {result} {toler}\n")

if __name__ == "__main__":
    main()
