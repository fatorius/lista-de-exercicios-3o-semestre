class Membro:
    def __init__(self, nome, pai):
        self.filhos = []
        self.nome = nome
        self.pai = pai

    def adicionarFilho(self, nome):
        self.filhos.append(Membro(nome, self))

    def encontrarParentesco(self, pessoa, raiz=True, membros_pesquisados=[]):
        encontrado = False
        linha_de_parentesco = ""

        membros_pesquisados.append(self.nome)

        if self.pai != None and not (self.pai.nome in membros_pesquisados):
            if self.pai.nome == pessoa:
                linha_de_parentesco = "filho do "
                encontrado = True
            else:
                parentesco_do_pai = self.pai.encontrarParentesco(pessoa, False, membros_pesquisados)
                if parentesco_do_pai != "nada do ":
                    linha_de_parentesco = "filho do " + parentesco_do_pai
                    encontrado = True

        if not encontrado:
            for filho in self.filhos:
                if filho.nome == pessoa and not (filho.nome in membros_pesquisados):
                    linha_de_parentesco = "pai do "
                    encontrado = True
                else:
                    parentesco_do_filho = filho.encontrarParentesco(pessoa, False, membros_pesquisados)
                    if parentesco_do_filho != "nada do ":
                        linha_de_parentesco = "pai do " + parentesco_do_filho

        if linha_de_parentesco == "":
            linha_de_parentesco = "nada do "

        if raiz:

            while True:
                alterado = False

                if linha_de_parentesco.find("filho do filho do ") != -1:
                    alterado = True
                    linha_de_parentesco = linha_de_parentesco.replace("filho do filho do ", "neto do ")
                
                if linha_de_parentesco.find("filho do pai do ") != -1:
                    alterado = True
                    linha_de_parentesco = linha_de_parentesco.replace("filho do pai do ", "tio do ")
            
                if not alterado:
                    break

            print(f"{self.nome} é {linha_de_parentesco}{pessoa}")
        else:
            return linha_de_parentesco

vo = Membro("João", None)

vo.adicionarFilho("Maria")
vo.adicionarFilho("Roberto")

vo.filhos[0].adicionarFilho("Lucas")
vo.filhos[0].adicionarFilho("Juliana")

vo.filhos[1].adicionarFilho("Julio")
vo.filhos[1].adicionarFilho("Felipe")

vo.filhos[1].filhos[1].encontrarParentesco("Maria")
