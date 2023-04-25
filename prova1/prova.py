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
    print("A biblioteca pandas não está instalada no seu computador. \n"
          + "Irei tentar instalar pandas automaticamente para você \n"
          + "Essa biblioteca é necessária para tratar de arquivos .xlsx \n"
          + "Se não der certo, por favor, instale manualmente executando o comando: \n"
          + "python3 -m pip install pandas")
    instalar_pacote("pandas")

try:
    from colorama import init

    init(autoreset=True)
except ModuleNotFoundError:
    print("A biblioteca colorama não está instalada no seu computador. \n"
          + "Irei tentar instalar colorama automaticamente para você \n"
          + "Essa biblioteca é necessária para usar exibir textos coloridos no seu terminal \n"
          + "Se não der certo, por favor, instale manualmente executando o comando: \n"
          + "python3 -m pip install colorama")
    instalar_pacote("colorama")

try:
    from termcolor import colored
except ModuleNotFoundError:
    print("A biblioteca termcolor não está instalada no seu computador. \n"
          + "Irei tentar instalar colorama automaticamente para você \n"
          + "Essa biblioteca é necessária para usar exibir textos coloridos no seu terminal \n"
          + "Se não der certo, por favor, instale manualmente executando o comando: \n"
          + "python3 -m pip install termcolor")
    instalar_pacote("termcolor")


def exibir_mensagens_de_boas_vindas():
    print(colored("Bem-vindo João Serasa!", "white"))


def menu_de_opcoes():
    print()

    print(colored("Digite a opção desejada: ", "white", "on_yellow"))
    print(colored("1 - Informar salario", "yellow"))
    print(colored("2 - Alterar salario", "yellow"))
    print(colored("3 - Excluir salario", "yellow"))
    print(colored("4 - Listar salarios", "yellow"))
    print(colored("5 - Informar despesa", "yellow"))
    print(colored("6 - Alterar despesa", "yellow"))
    print(colored("7 - Remover despesa", "yellow"))
    print(colored("8 - Listar despesas", "yellow"))
    print(colored("9 - Mostar resultado", "yellow"))
    print(colored("0 - Sair", "yellow"))

    print()

    try:
        opcao_selecionada = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Erro: Opção informada inválida", "red"))
        return menu_de_opcoes()

    if 0 <= opcao_selecionada < 10:
        return opcao_selecionada
    else:
        print(colored("Erro: Opção informada inválida", "red"))
        return menu_de_opcoes()


tabela = None
poupanca = None


def informar_salario():
    tamanho = tabela.shape[0]

    tipo_anterior = tabela.at[tamanho-1, "Tipo"]

    if (tipo_anterior == "Salario"):
        print(colored("ATENÇÃO: Você precisa informar as despesas do mês antes de informar o próximo salário", "white", "on_red"))
        return 

    mes_anterior = tabela.at[tamanho-1, "Mes"]
    ano_anterior = tabela.at[tamanho-1, "Ano"]

    mes_atual = mes_anterior + 1
    ano_atual = ano_anterior

    if mes_atual == 13:
        mes_atual = 1
        ano_atual += 1

    print(colored(f"Informe o seu salário para o mês {mes_atual} de {ano_atual}", "white", "on_blue"))

    salario_atual = 0

    try:
        salario_atual = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Salário digitado inválido, tente novamente: ", "red"))
        informar_salario()

    tabela.loc[tamanho] = {"Mes": mes_atual,"Ano": ano_atual,"Valor": salario_atual,"Tipo": "Salario"}
    
    print(colored(f"Salário adicionado com sucesso", "white", "on_blue"))


def excluir_salario():
    print(colored(f"ATENÇÃO -> Essa ação irá excluir todos os lançamentos subsequentes para evitar inconsistencias", "white", "on_red"))

    mes = 0
    ano = 0

    print(colored(f"Digite o mês a ser excluido", "white", "on_blue"))

    try:
        mes = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    print(colored(f"Digite o ano a ser excluido", "white", "on_blue"))
    
    try:
        ano = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    tamanho = tabela.shape[0]

    fim = 0

    for linha in range(tamanho):
        if tabela.at[linha, "Mes"] == mes and tabela.at[linha, "Ano"]:
            fim = linha
            break

    tabela = tabela.iloc[:fim]

    
def alterar_salario():
    mes = 0
    ano = 0

    print(colored(f"Digite o mês a ser alterado", "white", "on_blue"))

    try:
        mes = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    print(colored(f"Digite o ano a ser alterado", "white", "on_blue"))
    
    try:
        ano = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    print(colored(f"Digite o valor", "white", "on_blue"))
    
    valor = 0

    try:
        valor = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    tamanho = tabela.shape[0]

    fim = 0

    for linha in range(tamanho):
        if tabela.at[linha, "Mes"] == mes and tabela.at[linha, "Ano"]:
            fim = linha
            break

    tabela.at[fim, "Valor"] = valor


def listar_salario():
    print(colored(f"Os seus salários foram: ", "white", "on_blue"))

    tamanho = tabela.shape[0]

    for linha in range(tamanho):
        if tabela.at[linha, "Tipo"] == "Salario":
            mes = tabela.iloc[linha]["Mes"]
            ano = tabela.iloc[linha]["Ano"]
            valor = tabela.iloc[linha]["Valor"]

            print(f"Mês {mes} de {ano}: R$ {valor}")


def aplicar_na_poupanca(valor, mes, ano):
    print(colored(f"O valor de {valor} será aplicado no fundo de renda fixa", "white", "on_green"))

    tamanho = poupanca.shape[0]

    saldo_anterior = poupanca.at[tamanho-1, "Saldo"]

    rendimento = saldo_anterior  / 100

    poupanca.loc[tamanho] = {"Mes": mes,"Ano": ano,"Valor": valor,"Tipo": "Aplicação", "Saldo": saldo_anterior + valor}
    poupanca.loc[tamanho+1] = {"Mes": mes,"Ano": ano,"Valor": rendimento,"Tipo": "Rendimento", "Saldo": saldo_anterior + valor + rendimento}


def informar_despesa():
    tamanho = tabela.shape[0]

    tipo_anterior = tabela.at[tamanho-1, "Tipo"]

    if (tipo_anterior != "Salario"):
        print(colored("ATENÇÃO: Você precisa informar o salário do mês antes de informar as despesas", "white", "on_red"))
        return 

    mes_anterior = tabela.at[tamanho-1, "Mes"]
    ano_anterior = tabela.at[tamanho-1, "Ano"]
    salario_anterior = tabela.at[tamanho-1, "Valor"]

    print(colored(f"Informe as suas despesas para o mês {mes_anterior} de {ano_anterior}", "white", "on_red"))

    despesa_atual = 0

    try:
        despesa_atual = int(input(colored("joao-serasa: ~$ ", "light_green")))
        if salario_anterior < despesa_atual:
            print(colored("As despesas não podem ser maiores que as receitas, tente novamente: ", "red"))
            informar_despesa()

            return
    except:
        print(colored("Despesa digitada inválida, tente novamente: ", "red"))
        informar_despesa()

        return
        
    tabela.loc[tamanho] = {"Mes": mes_anterior,"Ano": ano_anterior,"Valor": despesa_atual,"Tipo": "Despesa"}
    
    print(colored(f"Despesas registradas com sucesso", "white", "on_red"))

    aplicar_na_poupanca(salario_anterior-despesa_atual, mes_anterior, ano_anterior)


def alterar_despesa():
    mes = 0
    ano = 0

    print(colored(f"Digite o mês a ser alterado", "white", "on_blue"))

    try:
        mes = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    print(colored(f"Digite o ano a ser alterado", "white", "on_blue"))
    
    try:
        ano = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    print(colored(f"Digite o valor", "white", "on_blue"))
    
    valor = 0

    try:
        valor = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    tamanho = tabela.shape[0]

    fim = 0

    for linha in range(tamanho):
        if tabela.at[linha, "Mes"] == mes and tabela.at[linha, "Ano"]:
            fim = linha
            break

    tabela.at[fim+1, "Valor"] = valor


def remover_despesa():
    print(colored(f"ATENÇÃO -> Essa ação irá excluir todos os lançamentos subsequentes para evitar inconsistencias", "white", "on_red"))

    mes = 0
    ano = 0

    print(colored(f"Digite o mês a ser excluido", "white", "on_blue"))

    try:
        mes = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    print(colored(f"Digite o ano a ser excluido", "white", "on_blue"))
    
    try:
        ano = int(input(colored("joao-serasa: ~$ ", "light_green")))
    except:
        print(colored("Valores de entrada inválidos, tente novamente: ", "red"))
        excluir_salario()
        return
    
    tamanho = tabela.shape[0]

    fim = 0

    for linha in range(tamanho):
        if tabela.at[linha, "Mes"] == mes and tabela.at[linha, "Ano"]:
            fim = linha
            break

    tabela = tabela.iloc[:fim]


def listar_despesas():
    print(colored(f"As suas despesas foram: ", "white", "on_red"))

    tamanho = tabela.shape[0]

    for linha in range(tamanho):
        if tabela.at[linha, "Tipo"] == "Despesa":
            mes = tabela.iloc[linha]["Mes"]
            ano = tabela.iloc[linha]["Ano"]
            valor = tabela.iloc[linha]["Valor"]

            print(f"Mês {mes} de {ano}: R$ {valor}")
    pass


def mostrar_resultados():
    print()
    print(colored("Receitas/Despesas Mes a Mes:", "black", "on_white"))
    print(tabela)
    
    print()
    print(colored("Investimentos Mes a Mes:", "black", "on_white"))
    print(poupanca)

    print()
    print(colored("Aperte enter para continuar", "white", "on_cyan"))
    input()


def carregar_tabela():
    global poupanca
    global tabela
    
    try:
        tabela = pd.read_csv("tabela.csv")
    except FileNotFoundError:
        with open("tabela.csv", 'w') as nova_tabela:
            nova_tabela.write("id,Mes,Ano,Valor,Tipo\n")
            nova_tabela.write('0,0,2023,0,Inicio')
            nova_tabela.close()

        tabela = pd.read_csv("tabela.csv", index_col="id")

    try:
        poupanca = pd.read_csv("poupanca.csv")
    except FileNotFoundError:
        with open("poupanca.csv", "w") as tabela_de_poupanca:
            tabela_de_poupanca.write("id,Mes,Ano,Valor,Tipo,Saldo\n")
            tabela_de_poupanca.write("0,0,2023,0,Inicio,0")
            tabela_de_poupanca.close()
        
        poupanca = pd.read_csv("poupanca.csv", index_col="id")
    

def encerrar_programa():
    print(colored("Encerrando programa...", "white", "on_red"))
    exit()

def iniciar_programa():
    carregar_tabela()

    exibir_mensagens_de_boas_vindas()

    while True:
        [encerrar_programa, informar_salario, alterar_salario, excluir_salario,
         listar_salario, informar_despesa, alterar_despesa, remover_despesa,
         listar_despesas, mostrar_resultados][menu_de_opcoes()]()
    
        tabela.to_csv("tabela.csv", index_label=False)
        poupanca.to_csv("poupanca.csv", index_label=False)

iniciar_programa()
