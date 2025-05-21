nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

if(media >= 6):
    situacao = "Arpovado"
else:
    if(media >= 4) and (media < 6):
        situacao = "Reciperação"
    else:
        situacao = "Reprovado!"

print(f"{nome} a média é: {media} e você está {situacao}")