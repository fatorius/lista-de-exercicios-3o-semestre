class Membro:
    def __init__(self, nome, pai):
        self.filhos = []
        self.nome = nome
        self.pai = pai

    def adicionarFilho(self, nome):
        self.filhos.append(Membro(nome, self))

    def encontrarParentesco(self, pessoa):
        fila_de_pesquisa = [self.pai] + self.filhos

        while (len(fila_de_pesquisa) > 0):
            # procurar  
            proximo_candidato = fila_de_pesquisa.pop(0)


            # expandir



# Use the insert method to add Membros
vo = Membro("João", None)

vo.adicionarFilho("Maria")
vo.adicionarFilho("Roberto")

vo.filhos[0].adicionarFilho("Lucas")
vo.filhos[0].adicionarFilho("Juliana")

vo.filhos[1].adicionarFilho("Julio")
vo.filhos[1].adicionarFilho("Felipe")
