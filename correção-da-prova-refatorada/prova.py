# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:43:17 2023

@author: wellynton, hugosouza
"""

from datetime import datetime
from dateutil import relativedelta

from funcoes.inputs import informar_inteiro
from funcoes.inputs import informar_float
from funcoes.arquivos import Arquivo


def retornar_saldo(ano, mes):
    with open('salario.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            registro = linha.split(',')
            if ano == int(registro[0]) and mes == int(registro[1]):
                return registro[2]


def buscar_total_despesa(ano, mes):
    with open('despesa.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        total = 0
        for linha in linhas:
            registro = linha.split(',')
            if int(ano) == int(registro[0]) and int(mes) == int(registro[1]):
                total = registro[2]

        return total


def calcular_rendimento(valor, ano, mes):
    d1 = '01/' + mes + '/' + ano
    d2 = '01/' + str(datetime.now().month) + '/' + str(datetime.now().year)

    start_date = datetime.strptime(d1, "%d/%m/%Y")
    end_date = datetime.strptime(d2, "%d/%m/%Y")

    delta = relativedelta.relativedelta(end_date, start_date)
    total_meses = delta.months + (delta.years * 12)
    taxa = 0.01
    return valor * (1 + taxa) ** total_meses


def encerrar_programa():
    exit(0)


def informar_salario():
    arquivo = Arquivo("salario.txt")
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')
    salario = informar_float('Informe o salário: ')

    arquivo.adionar_linha(str(ano) + ',' + str(mes) + ',' + str(salario))


def alterar_salario():
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')
    salario = informar_float('Informe o novo salário: ')

    linha_alterada = 0

    arquivo = Arquivo("salario.txt")

    linhas = arquivo.linhas_do_arquivo

    for linha in linhas:
        registro = linha.split(',')
        if ano == int(registro[0]) and mes == int(registro[1]):
            linha_alterada = linhas.index(linha)

    linhas[linha_alterada] = str(ano) + ',' + str(mes) + ',' + str(salario) + '\n'

    arquivo.reescrever_arquivo(linhas)


def excluir_salario():
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')

    linha_alterada = 0

    arquivo = Arquivo("salario.txt")
    linhas = arquivo.linhas_do_arquivo

    for linha in linhas:
        registro = linha.split(',')
        if ano == int(registro[0]) and mes == int(registro[1]):
            linha_alterada = linhas.index(linha)

    linhas.pop(linha_alterada)
    arquivo.reescrever_arquivo(linhas)


def listar_salarios():
    arquivo = Arquivo("salario.txt")
    linhas = arquivo.linhas_do_arquivo

    linhas.sort()

    print(linhas)
    print('----Salários----')

    for linha in linhas:
        registro = linha.split(',')
        print('Ano: ' + registro[0] + ' Mês: ' + registro[1] + ' Salário: ' + registro[2])


def informar_despesa():
    ano = informar_inteiro('Informe o ano: ')
    mes = informar_inteiro('Informe o mês: ')
    despesa = informar_float('Informe a despesa: ')

    saldo_mes = float(retornar_saldo(ano, mes))

    if despesa > saldo_mes:
        print('Saldo insuficiente!')
        return

    arquivo = Arquivo("despesa.txt")
    arquivo.adionar_linha(str(ano) + ',' + str(mes) + ',' + str(despesa) + ';')


def alterar_despesa():
    pass


def remover_despesa():
    pass


def listar_despesas():
    arquivo = Arquivo("despesas.txt")
    linhas = arquivo.linhas_do_arquivo

    linhas.sort()

    print(linhas)
    print('----Despesas----')

    for linha in linhas:
        registro = linha.split(',')
        print('Ano: ' + registro[0] + ' Mês: ' + registro[1] + ' Despesa: ' + registro[2])


def mostar_resultado():
    with open('salario.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
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


def opcao_do_usuario():
    print("Informe a opção desejada: ")

    print("1 - Informar salario")
    print("2 - Alterar salario")
    print("3 - Excluir salario")
    print("4 - Listar salarios")
    print("5 - Informar despesa")
    print("6 - Alterar despesa")
    print("7 - Remover despesa")
    print("8 - Listar despesas")
    print("9 - Mostar resultado")
    print("0 - Sair")

    return int(input())


def main():
    while True:
        [
            encerrar_programa,
            informar_salario, alterar_salario, excluir_salario,
            listar_salarios, informar_despesa, alterar_despesa,
            remover_despesa, listar_despesas, mostar_resultado
        ][opcao_do_usuario()]()


main()
