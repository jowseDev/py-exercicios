tipo = str(input("Digite G para Gasolina \n ou \n A para Alcool: \n"))
tq = float(input("Digite a capacidade do tanque: \n"))

if(tipo == "G"):
    v = int(input("Voçê escolheu Gasolina: \n Digite o valor da Gasolina:"))
    print(f"O valor para encher o tanque ficará em: R${v * tq}")
elif(tipo == "A"):
    v = int(input("Voçê escolheu Alcool: \n Digite o valor do Alcool: "))
    print(f"O valor para encher o tanque ficará em: R${v * tq}")
else:
    print("Letra invalidada:")


