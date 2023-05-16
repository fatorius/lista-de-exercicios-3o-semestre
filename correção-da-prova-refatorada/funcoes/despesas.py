from inputs import *
from arquivos import *

arquivo_salario = Arquivo("salario.txt")
arquivo_despesa = Arquivo("despesa.txt")


def buscar_total_despesa(ano, mes):
    linhas = arquivo_despesa.linhas_do_arquivo
    total = 0
    for linha in linhas:
        registro = linha.split(',')
        if int(ano) == int(registro[0]) and int(mes) == int(registro[1]):
            total = registro[2]

    return total


def retornar_saldo(ano, mes):
    linhas = arquivo_salario.linhas_do_arquivo
    for linha in linhas:
        registro = linha.split(',')
        if ano == int(registro[0]) and mes == int(registro[1]):
            return registro[2]


def informar_despesa():
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')
    despesa = informar_float('Informe a despesa: ')

    saldo_mes = float(retornar_saldo(ano, mes))

    if despesa > saldo_mes:
        print('Saldo insuficiente!')
        return

    arquivo_despesa.adionar_linha(str(ano) + ',' + str(mes) + ',' + str(despesa) + ';')


def alterar_despesa():
    pass


def remover_despesa():
    pass


def listar_despesas():
    linhas = arquivo_despesa.linhas_do_arquivo

    linhas.sort()

    print(linhas)
    print('----Despesas----')

    for linha in linhas:
        registro = linha.split(',')
        print('Ano: ' + registro[0] + ' Mês: ' + registro[1] + ' Despesa: ' + registro[2])
