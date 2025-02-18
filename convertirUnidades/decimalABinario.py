def femboy(numDecimal):
    return bin(numDecimal)[2:]

numeroEnDecimal = int(input("Mete el decimal imbécil: "))
numeroEnBinario = femboy(numeroEnDecimal)
print(f"{numeroEnDecimal} -> {numeroEnBinario}")
