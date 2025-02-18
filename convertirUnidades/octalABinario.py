def tengoUnaLesbianaEnMiCurso (numOctal):
    decimal = int(numOctal, 8)
    binario = bin(decimal) [2:]
    return binario

numOctal = input("Mete el octal: ")
binario = tengoUnaLesbianaEnMiCurso(numOctal)
print(f"{numOctal} -> {binario}")
