class Categoria:
    def __init__(self, nome, pai):
        self.subcategorias = []
        self.nome = nome
        self.pai = pai

    def adicionarSubcategoria(self, nome):
        self.subcategorias.append(Categoria(nome, self))

    def imprimirSubcategorias(self, raiz=True):
        if raiz:
            print(f"Subcategorias de {self.nome}: ")
        
        for subs in self.subcategorias:
            subs.imprimirSubcategorias(False)

        print(self.nome)

raiz = Categoria("Site", None)

raiz.adicionarSubcategoria("Sub1")
raiz.adicionarSubcategoria("Sub2")

raiz.subcategorias[0].adicionarSubcategoria("Cat1")
raiz.subcategorias[0].adicionarSubcategoria("Cat2")

raiz.subcategorias[1].adicionarSubcategoria("Cat3")
raiz.subcategorias[1].adicionarSubcategoria("Cat4")

raiz.imprimirSubcategorias()