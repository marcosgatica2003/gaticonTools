def marianoViolin(numHexa):
    numDec = int(numHexa, 16)
    numBinario = bin(numDec)[2:]
    return numBinario

numHexa = input("Mete el hexa sin 0x: ")
binario = marianoViolin(numHexa)
print(f"{numHexa} -> {binario}")
