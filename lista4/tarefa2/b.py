numeros = []

def adicionarNumero(numero):
    numeros.append(numero)
    print(f"O numero {numero} foi adicionado")
    print(f"A fila agora é {numeros}")

def removerPrimeiroNumero():
    print(f"O numero {numeros.pop(0)} foi removido")
    print(f"A fila agora é {numeros}")

adicionarNumero(1)
adicionarNumero(2)
adicionarNumero(3)
adicionarNumero(4)
adicionarNumero(5)
adicionarNumero(6)
removerPrimeiroNumero()
removerPrimeiroNumero()
removerPrimeiroNumero()
removerPrimeiroNumero()
removerPrimeiroNumero()