cn = 1
vtotal = 0
em9 = 0
em12 = 0
em23 = 0
em40 = 0

while (cn != 0):
    cn = int(input("Digite o canal para a pesquisa: \n Caso deseje sair Digite o canal 0 \n"))
    if(cn == 9 or cn == 12 or cn == 23 or cn == 40):
        if(cn == 9):
            em9 = em9 + 1
        if(cn == 12):
            em12 = em12 + 1
        if(cn == 23):
            em23 = em23 + 1
        if(cn == 40):
            em40 = em40 + 1
    else:
        print("Numero invalido!")

    print(em9, "\n", em12, "\n", em23, "\n", em40 )
    
vtotal = em9 + em12 + em23 + em40
print("Porcentagem de Espectadores: \n")
print("Canal 9: ", (em9 / vtotal) * 100, "%")
print("Canal 12: ", (em12 / vtotal) * 100, "%")
print("Canal 23: ", (em23 / vtotal) * 100, "%")
print("Canal 40: ", (em40 / vtotal) * 100, "%")
