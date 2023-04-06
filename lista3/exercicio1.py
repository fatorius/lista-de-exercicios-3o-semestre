class NumeroImpar(Exception):
    def __init__(self):
        self.mensagem = "Falei pra você que o número devia ser par"

try: 
    numero = int(input("Digite um número par: "))

    if (numero % 2 == 1):
        raise NumeroImpar

    print(numero)
except NumeroImpar as e:
    print(e.mensagem)