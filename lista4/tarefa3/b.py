numeros = []

def adicionarNumero(numero):
    numeros.append(numero)
    print(f"O numero {numero} foi adicionado")
    print(f"A pilha agora é {numeros}")

def removerNumeroDoTopo():
    print(f"O numero {numeros.pop()} foi removido")
    print(f"A pilha agora é {numeros}")

adicionarNumero(1)
adicionarNumero(2)
adicionarNumero(3)
adicionarNumero(4)
adicionarNumero(5)
adicionarNumero(6)

removerNumeroDoTopo()
removerNumeroDoTopo()
removerNumeroDoTopo()
removerNumeroDoTopo()
removerNumeroDoTopo()
removerNumeroDoTopo()