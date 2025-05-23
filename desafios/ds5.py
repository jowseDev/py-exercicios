# Exercício 7 – Média de várias notas
# Peça 5 notas e calcule a média.

soma = 0
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma / 5
print(f"A média é: {media}")
