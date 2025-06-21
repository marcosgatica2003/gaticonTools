#!/bin/python3
import sys

bandValues = {
    'negro': 0, 'marron': 1, 'rojo': 2, 'naranja': 3,
    'amarillo': 4, 'verde': 5, 'azul': 6, 'violeta': 7,
    'gris': 8, 'blanco': 9
}

multipliers = {
    'negro': 1, 'marron': 10, 'rojo': 100, 'naranja': 1_000,
    'amarillo': 10_000, 'verde': 100_000, 'azul': 1_000_000,
    'violeta': 10_000_000, 'gris': 100_000_000, 'blanco': 1_000_000_000,
    'dorado': 0.1, 'plateado': 0.01
}

toleranceValues = {
    'marron': '±1%', 'rojo': '±2%', 'dorado': '±5%', 'plateado': '±10%'
}

def formatResistance(ohmValue):
    if ohmValue >= 1_000_000:
        return f"{ohmValue/1_000_000:.2f} MΩ"
    if ohmValue >= 1_000:
        return f"{ohmValue/1_000:.2f} kΩ"
    return f"{ohmValue:.2f} Ω"

def calculateResistance(band1, band2, multiplierColor):
    digits = bandValues[band1] * 10 + bandValues[band2]
    return digits * multipliers[multiplierColor]

def main():
    print("Hola Rao\nCalculadora de resistencias de 4 bandas")
    print("Mete 'salir' para salir pos p hijito.\n")
    while True:
        band1 = input("1) Primer color: ").strip().lower()
        if band1 == 'salir': print("¡Hasta luego!"); sys.exit()
        band2 = input("2) Segundo color: ").strip().lower()
        if band2 == 'salir': print("¡Hasta luego!"); sys.exit()
        mult = input("3) Color multiplicador: ").strip().lower()
        if mult == 'salir': print("¡Hasta luego!"); sys.exit()
        tol = input("4) Tolerancia (opcional): ").strip().lower()
        if tol == 'salir': print("¡Hasta luego!"); sys.exit()
        try:
            ohm = calculateResistance(band1, band2, mult)
        except KeyError:
            print("\nColor no válido.\n")
            continue
        result = formatResistance(ohm)
        toler = toleranceValues.get(tol, '')
        print(f"\n→ Resistencia: {result} {toler}\n")

if __name__ == "__main__":
    main()

