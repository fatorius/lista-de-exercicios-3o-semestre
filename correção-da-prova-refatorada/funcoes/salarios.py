from inputs import *
from arquivos import *

from datetime import datetime
from dateutil import relativedelta

arquivo_salario = Arquivo("salario.txt")


def informar_salario():
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')
    salario = informar_float('Informe o salário: ')

    arquivo_salario.adionar_linha(str(ano) + ',' + str(mes) + ',' + str(salario))


def alterar_salario():
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')
    salario = informar_float('Informe o novo salário: ')

    linha_alterada = 0

    linhas = arquivo_salario.linhas_do_arquivo

    for linha in linhas:
        registro = linha.split(',')
        if ano == int(registro[0]) and mes == int(registro[1]):
            linha_alterada = linhas.index(linha)

    linhas[linha_alterada] = str(ano) + ',' + str(mes) + ',' + str(salario) + '\n'

    arquivo_salario.reescrever_arquivo(linhas)


def excluir_salario():
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')

    linha_alterada = 0

    linhas = arquivo_salario.linhas_do_arquivo

    for linha in linhas:
        registro = linha.split(',')
        if ano == int(registro[0]) and mes == int(registro[1]):
            linha_alterada = linhas.index(linha)

    linhas.pop(linha_alterada)
    arquivo_salario.reescrever_arquivo(linhas)


def listar_salarios():
    linhas = arquivo_salario.linhas_do_arquivo

    linhas.sort()

    print(linhas)
    print('----Salários----')

    for linha in linhas:
        registro = linha.split(',')
        print('Ano: ' + registro[0] + ' Mês: ' + registro[1] + ' Salário: ' + registro[2])


def mostar_resultado():
    linhas = arquivo_salario.linhas_do_arquivo
    linhas.sort()
    print(linhas)
    print('----Salários----')
    for linha in linhas:
        registro = linha.split(',')
        print('Ano: ' + registro[0] + ' Mês: ' + registro[1])
        salario = float(registro[2])
        print('Salário: ' + str(salario))
        total_despesa = buscar_total_despesa(registro[0], registro[1])
        print('Despesa: ', total_despesa)
        saldo = salario - float(total_despesa)
        print('Saldo: ', saldo)
        bateu_meta = saldo > (salario * 0.1)
        print('Meta: ', bateu_meta)
        print('Valor investido: ', saldo)
        rendimento = calcular_rendimento(saldo, registro[0], registro[1])
        print('Rendimento: ', rendimento)


def calcular_rendimento(valor, ano, mes):
    d1 = '01/' + mes + '/' + ano
    d2 = '01/' + str(datetime.now().month) + '/' + str(datetime.now().year)

    start_date = datetime.strptime(d1, "%d/%m/%Y")
    end_date = datetime.strptime(d2, "%d/%m/%Y")

    delta = relativedelta.relativedelta(end_date, start_date)
    total_meses = delta.months + (delta.years * 12)
    taxa = 0.01
    return valor * (1 + taxa) ** total_meses
