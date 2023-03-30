with open("exame.txt") as exame:
    valores = exame.readlines()

    total_de_alunos = len(valores) // 3

    for a in range(total_de_alunos):
        aluno = a * 3
        nota_exame = int(input("Digite a nova nota de exame do aluno " + valores[aluno] + ": "))

        media_final = (nota_exame + float(valores[aluno+1][:-2])) / 2

        if media_final >= 5:
            print("Aluno aprovado")

            with open("aprovados.txt", "a+") as file:
                file.write(valores[aluno].strip() + " - Aprovado após exame\n")
                file.write(str(media_final) + "\n")
                file.write("="*10 + "\n")
                file.close()
        else:
            print("Aluno reprovado")

            with open("reprovados.txt", "a+") as file:
                file.write(valores[aluno] + " - Reprovado após exame\n")
                file.write(media_final + "\n")
                file.write("="*10 + "\n")
                file.close()
    exame.close()

                