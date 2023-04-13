class No:
    def __init__(self, nome):
      self.esq = None
      self.dir = None
      self.nome = nome

    def inserirFilme(self, novoFilme):
      if self.nome:
         if novoFilme < self.nome:
            if self.esq is None:
               self.esq = No(novoFilme)
            else:
               self.esq.inserirFilme(novoFilme)
         elif novoFilme > self.nome:
               if self.dir is None:
                  self.dir = No(novoFilme)
               else:
                  self.dir.inserirFilme(novoFilme)
      else:
         self.nome = novoFilme

    def obterLista(self):
        lista = []
        if self.esq:
            lista += self.esq.obterLista()
        else:
           lista.append(self.nome)
        if self.dir:
            lista += self.dir.obterLista()
        else:
           lista.append(self.nome)

        return lista
    
    def obterFilmeAlfabeticoApos(self, filme):
        listaDeFilmes = self.obterLista()
        
        if not filme in listaDeFilmes:
           print(f"{filme} não está presente na árvore")
        else:
           print(f"O filme que aparece após {filme} é {listaDeFilmes[listaDeFilmes.index(filme) + 1]}")


# Use the insert method to add nodes
root = No("O Senhor dos Aneis")
root.inserirFilme("O Hobbit")
root.inserirFilme("Star War")
root.inserirFilme("Shrek")
root.inserirFilme("Barbie")
root.inserirFilme("Adam Sandler")
root.inserirFilme("Os três Mosqueteiros")
root.inserirFilme("Vingadores")

root.obterFilmeAlfabeticoApos("Barbie")
root.obterFilmeAlfabeticoApos("Star Trek")