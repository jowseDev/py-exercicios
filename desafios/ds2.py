# Desafio 2 – Maior número
# Peça dois números e diga qual é o maior ou se são iguais.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if(n1 > n2):
    print(f"{n1} É o maior numero!")
elif(n1 < n2):
    print(f"{n2} É o maior numero!")
elif(n1 == n2):
    print("Os dois numeros sao iguais!")
else:
    print("Isso nao é um numero!")