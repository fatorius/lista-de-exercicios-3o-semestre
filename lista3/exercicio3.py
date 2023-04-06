try:
    divisor = int(input("Digite um numero para ser o divisor da fração: "))

    divisao = 10 / divisor
except ZeroDivisionError:
    print("Não podemos dividir por zero")