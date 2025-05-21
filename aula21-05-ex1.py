nome = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0

nome = input("Informe o nome do aluno: ")
nota1 = float(input("Digite o primeiro numero:"))
nota2 = float(input("Digite o primeiro numero:"))

media = (nota1 + nota2) / 2

print(f"{nome}, a sua media de notas é: {media}")