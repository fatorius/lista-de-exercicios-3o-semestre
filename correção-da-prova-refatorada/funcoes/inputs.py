def informar_float(mensagem):
    try:
        valor = float(input(mensagem))
        return valor
    except ValueError:
        print('inválido!')
        return informar_float(mensagem)


def informar_inteiro(mensagem):
    try:
        valor = int(input(mensagem))
        return valor
    except ValueError:
        print('inválido!')
        return informar_inteiro(mensagem)
