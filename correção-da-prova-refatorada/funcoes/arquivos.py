class Arquivo:
    def __init__(self, nome_do_arquivo):

        self.linhas_do_arquivo = []
        self.nome_do_arquivo = nome_do_arquivo

        with open(nome_do_arquivo, "r+") as arquivo:
            self.linhas_do_arquivo = arquivo.readlines()
            arquivo.close()

    def adionar_linha(self, linha: str):
        with open(self.nome_do_arquivo, "a+") as arquivo:
            arquivo.write(linha)
            arquivo.write("\n")
            arquivo.close()

        self.linhas_do_arquivo.append(linha)

    def reescrever_arquivo(self, linhas: list):
        with open(self.nome_do_arquivo, "w+") as arquivo:
            arquivo.writelines(linhas)
            arquivo.close()

        self.linhas_do_arquivo = linhas
