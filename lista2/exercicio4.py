with open("aprovados.txt", "r") as aprovados:
    nomes = aprovados.readlines()

    for a in range(len(nomes)//3):
        print("Aprovado: " + nomes[a*3])
    
    aprovados.close()

with open("reprovados.txt", "r") as reprovados:
    nomes = reprovados.readlines()

    for a in range(len(nomes)//3):
        print("Reprovado: " + nomes[a*3])
    
    reprovados.close()