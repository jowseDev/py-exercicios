n1 = 0
n2 = 0
n3 = 0
r = 0

def produto(nm1, nm2, nm3):

    rs3 = (nm1 * nm2) * nm3
    rs2 = (nm1 + nm2) + nm3
    return rs2, rs3

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))
r2, r3 = produto(n1, n2, n3)
print(f"O resultado da soma é: {r2}")
print(f"O resultado da soma é: {r3}")