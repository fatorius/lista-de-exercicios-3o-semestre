with open("notas.txt", "a+") as notas:
    while True:
        nome = input("Digite o nome: ")
        n1 = input("Digite a nota 1: ")
        n2 = input("Digite a nota 2: ")
        n3 = input("Digite a nota 3: ")
    
        notas.write(nome + "\n")
        notas.write(n1 + "\n")
        notas.write(n2 + "\n")
        notas.write(n3 + "\n")
        notas.write("="*10 + "\n")
    
        if input("Deseja continuar [S/N] ").upper() != "S":
            break

    notas.close()

