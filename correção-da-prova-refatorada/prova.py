# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:43:17 2023

@author: wellynton, hugosouza
"""


from funcoes.despesas import *
from funcoes.salarios import *


def encerrar_programa():
    exit(0)


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
