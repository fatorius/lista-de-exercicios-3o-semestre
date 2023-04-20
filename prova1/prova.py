import pip
import sys
from os import execl
from subprocess import check_call


def instalar_pacote(pacote):
    try:
        pip.main(["install", pacote])
    except AttributeError:
        check_call([sys.executable, '-m', 'pip', 'install', pacote])

    execl(sys.executable, sys.executable, *sys.argv)


try:
    import pandas as pd
except ModuleNotFoundError:
    print("A biblioteca pandas não está instalada no seu computador. "
          + "Irei tentar instalar pandas automaticamente para você "
          + "Essa biblioteca é necessária para tratar de arquivos .xlsx "
          + "Se não der certo, por favor, instale manualmente executando o comando: "
          + "python3 -m pip install pandas")
    instalar_pacote("pandas")

try:
    from colorama import init

    init(autoreset=True)
except ModuleNotFoundError:
    print("A biblioteca colorama não está instalada no seu computador. "
          + "Irei tentar instalar colorama automaticamente para você "
          + "Essa biblioteca é necessária para usar exibir textos coloridos no seu terminal "
          + "Se não der certo, por favor, instale manualmente executando o comando: "
          + "python3 -m pip install colorama")
    instalar_pacote("colorama")

try:
    from termcolor import colored
except ModuleNotFoundError:
    print("A biblioteca termcolor não está instalada no seu computador. "
          + "Irei tentar instalar colorama automaticamente para você "
          + "Essa biblioteca é necessária para usar exibir textos coloridos no seu terminal "
          + "Se não der certo, por favor, instale manualmente executando o comando: "
          + "python3 -m pip install termcolor")
    instalar_pacote("termcolor")


def exibir_mensagens_de_boas_vindas():
    print(colored("Bem-vindo João Serasa!", "white"))


def menu_de_opcoes():
    print(colored("Digite a opção desejada: ", "white", "on_yellow"))
    print(colored("1 - Informar salario", "yellow"))
    print(colored("2 - Alterar salario", "yellow"))
    print(colored("3 - Excluir salario", "yellow"))
    print(colored("4 - Listar salarios", "yellow"))
    print(colored("5 - Informar despesa", "yellow"))
    print(colored("6 - Alterar despesa", "yellow"))
    print(colored("7 - Remover despesa", "yellow"))
    print(colored("8 - Listar despesa", "yellow"))
    print(colored("9 - Mostar resultado", "yellow"))

    try:
        opcao_selecionada = int(input(">> "))
    except:
        print(colored("Erro: Opção informada inválida", "red"))
        return menu_de_opcoes()

    if 0 < opcao_selecionada < 10:
        return opcao_selecionada
    else:
        print(colored("Erro: Opção informada inválida", "red"))
        return menu_de_opcoes()


tabela = None


def informar_salario():
    tamanho = tabela.shape[0]
    saldo_anterior = tabela.at[tamanho-1, "Saldo"]
    mes_anterior = tabela.at[tamanho-1, "Mes"]
    ano_anterior = tabela.at[tamanho-1, "Ano"]

    mes_atual = mes_anterior + 1
    ano_atual = ano_anterior

    if mes_atual == 13:
        mes_atual = 1
        ano_atual += 1

    print(colored(f"Informe o seu salário para o mês {mes_atual} de {ano_atual}", "white", "on_green"))

    salario_atual = 0

    try:
        salario_atual = int(input())
    except:
        print(colored("Salário digitado inválido, tente novamente: ", "red"))
        informar_salario()

    tabela.loc[tamanho] = {"Mes": mes_atual,"Ano": ano_atual,"Valor": salario_atual,"Tipo": "Salario",
                            "Saldo": saldo_anterior + salario_atual}

    tabela.to_csv("tabela.csv")

def excluir_salario():
    pass


def alterar_salario():
    pass


def listar_salario():
    pass


def informar_despesa():
    pass


def alterar_despesa():
    pass


def remover_despesa():
    pass


def listar_despesas():
    pass


def mostrar_resultados():
    pass


def carregar_tabela():
    global tabela
    try:
        tabela = pd.read_csv("tabela.csv")
    except FileNotFoundError:
        with open("tabela.csv", 'w') as nova_tabela:
            nova_tabela.write("Mes, Ano, Valor, Tipo, Saldo\n")
            nova_tabela.write('0, 0, 0, "Inicio", 0')
            nova_tabela.close()

        tabela = pd.read_csv("tabela.csv")


def iniciar_programa():
    carregar_tabela()

    exibir_mensagens_de_boas_vindas()

    ["", informar_salario, alterar_salario, excluir_salario,
     listar_salario, informar_despesa, alterar_despesa, remover_despesa,
     listar_despesas, mostrar_resultados][menu_de_opcoes()]()


iniciar_programa()
