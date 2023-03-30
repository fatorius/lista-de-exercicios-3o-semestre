with open("notas.txt", "r") as notas:
    valores = notas.readlines()

    total_de_alunos = len(valores) // 5

    for a in range(total_de_alunos):
        aluno = a * 5
        nome =  valores[aluno]
        n1 = int(valores[aluno+1])
        n2 = int(valores[aluno+2])
        n3 = int(valores[aluno+3])

        media = (n1+n2+n3) / 3

        estado = ""

        if (media >= 7):
            estado = "aprovados"
        elif (media >= 5):
            estado = "exame"
        else:
            estado = "reprovados"
    
        with open(estado + ".txt", "a+") as file:
            file.write(nome)
            file.write(str(media) + "\n")
            file.write("="*10 + "\n")
            file.close()

    notas.close()