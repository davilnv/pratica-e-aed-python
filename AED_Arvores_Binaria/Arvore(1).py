class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None

    def get_elemento(self):
        return self.elemento

    def set_elemento(self, elemento):
        self.elemento = elemento

    def get_esquerda(self):
        return self.esquerda

    def set_esquerda(self, esquerda):
        self.esquerda = esquerda

    def get_direita(self):
        return self.direita

    def set_direita(self, direita):
        self.direita = direita


class Arvore:
    def __init__(self):
        self.raiz = None
        self.__tamanho = 0

    def inserir(self, elemento):
        no = No(elemento)
        if self.vazia():
            self.raiz = no
        else:
            no_pai = None
            no_atual = self.raiz
            while True:
                if no_atual is not None:
                    no_pai = no_atual
                    if no.get_elemento() < no_atual.get_elemento():
                        no_atual = no_atual.get_esquerda()
                    else:
                        no_atual = no_atual.get_direita()
                else:
                    if no.get_elemento() < no_pai.get_elemento():
                        no_pai.set_esquerda(no)
                    else:
                        no_pai.set_direita(no)
                    break
        self.__tamanho += 1

    def remover(self, elemento):
        if self.vazia():
            raise ValueError("Arvore vazia")
        no_pai, no_atual = self.raiz, self.raiz
        filho_esquerdo = True
        while no_atual.get_elemento() != elemento:
            no_pai = no_atual
            if elemento < no_atual.get_elemento():
                no_atual = no_atual.get_esquerda()
                filho_esquerdo = True
            else:
                no_atual = no_atual.get_direita()
                filho_esquerdo = False
            if no_atual is None:
                return False
        # 1 Caso
        if no_atual.get_esquerda() is None and no_atual.get_direita() is None:
            if no_atual == self.raiz:
                self.raiz = None
            else:
                if filho_esquerdo:
                    no_pai.set_esquerda(None)
                else:
                    no_pai.set_direita(None)
        # 2 Caso
        elif no_atual.get_direita() is None:
            if self.raiz == no_atual:
                self.raiz = no_atual.get_esquerda()
            else:
                if filho_esquerdo:
                    no_pai.set_esquerda(no_atual.get_esquerda())
                    no_atual = None
                else:
                    no_pai.set_direita(no_atual.get_esquerda())
                    no_atual = None
        elif no_atual.get_esquerda is None:
            if self.raiz == no_atual:
                self.raiz = no_atual.get_direita()
            else:
                if filho_esquerdo:
                    no_pai.set_esquerda(no_atual.get_direita())
                    no_atual = None
                else:
                    no_pai.set_direita(no_atual.get_direita())
                    no_atual = None
        # 3 Caso
        else:
            novo_no = self.sucessor(no_atual)
            if no_atual == self.raiz:
                self.raiz = novo_no
            else:
                if filho_esquerdo:
                    no_pai.set_esquerda(novo_no)
                else:
                    no_pai.set_direita(novo_no)
            novo_no.set_esquerda(no_atual.get_esquerda())
            no_atual = None
        return True

    def __buscar(self, elemento, no_pai, no_atual):
        if no_atual is not None:
            if no_atual.get_elemento() == elemento:
                return no_pai, no_atual
            elif elemento < no_atual.get_elemento():
                self.__buscar(elemento, no_atual, no_atual.get_esquerda())
            else:
                self.__buscar(elemento, no_atual, no_atual.get_direita())
        else:
            raise RecursionError("Erro de recursão")

    def buscar(self, elemento):
        return self.__buscar(elemento, self.raiz, self.raiz)

    def vazia(self):
        if self.raiz is None:
            return True
        return False

    def __mostrar_no(self, no):
        if no is not None:
            self.__mostrar_no(no.get_esquerda())
            print(no.get_elemento(), end=" ")
            self.__mostrar_no(no.get_direita())

    def mostrar(self):
        self.__mostrar_no(self.raiz)
        print()

    def get_raiz(self):
        return self.raiz

    def get_tamanho(self):
        return self.__tamanho

    def get_minimo(self, raiz):
        if self.vazia():
            raise ValueError("A árvore está vazia!")
        else:
            no_atual = raiz
            while no_atual.get_esquerda() is not None:
                no_atual = no_atual.get_esquerda()
            return no_atual.get_elemento()

    def get_maximo(self, raiz):
        if self.vazia():
            raise ValueError("A árvore está vazia!")
        else:
            no_atual = raiz
            while no_atual.get_direita() is not None:
                no_atual = no_atual.get_direita()
            return no_atual.get_elemento()

    def predecessor(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        if raiz.get_esquerda() is not None:
            return self.get_maximo(raiz.get_esquerda())

    def sucessor(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        if raiz.get_direita() is not None:
            return self.get_minimo(raiz.get_direita())
