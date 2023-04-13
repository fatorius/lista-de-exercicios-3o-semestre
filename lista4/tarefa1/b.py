numeros = []

def adicionarNoInicio(numero):
    numeros.insert(0, numero)
    print(f"O número {numero} foi inserido no começo da lista")
    print(f"A lista atual é {numeros}")

def adicionarNoFinal(numero):
    numeros.append(numero)
    print(f"O número {numero} foi inserido no final da lista")
    print(f"A lista atual é {numeros}")

adicionarNoInicio(100)
adicionarNoInicio(300)
adicionarNoInicio(400)
adicionarNoFinal(900)
adicionarNoFinal(1000)
adicionarNoFinal(200)
adicionarNoFinal(500)