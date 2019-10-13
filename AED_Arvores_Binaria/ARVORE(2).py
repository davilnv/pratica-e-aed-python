class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.elemento)


class Arvore:
    def __init__(self):
        self.raiz = None
        self.__quantFolhas = 0
        self.nivel = 0

    def add(self, elemento):
        no = No(elemento)
        perc = self.raiz
        if self.vazio():
            self.raiz = no
        else:
            while True:
                if no.elemento > perc.elemento:
                    if perc.direita != None:
                        perc = perc.direita
                    else:
                        perc.direita = no
                        break
                elif no.elemento < perc.elemento:
                    if perc.esquerda != None:
                        perc = perc.esquerda
                    else:
                        perc.esquerda = no
                        break
                else:
                    raise Exception("Elemento já adicionado na lista")
        self.__quantFolhas += 1

        # QUANTOS NÍVEIS TEM A ÁRVORE

    def Remover(self, elemento):
        if self.raiz == None:
            raise ValueError("Arvore vazia")
        perc = self.raiz  # no elemento
        pai = self.raiz  # pai do elemento
        filho_esquerdo = True
        while perc.elemento != elemento:
            pai = perc
            if elemento < perc.elemento:
                perc = perc.esquerda
                filho_esquerdo = True
            else:
                perc = perc.direita
                filho_esquerdo = False
            if perc == None:
                return False
        if perc.esquerda is None and perc.direita is None:
            if perc == self.raiz:
                self.raiz = None
            else:
                if filho_esquerdo:
                    pai.esquerda = None
                else:
                    pai.direita = None
        elif perc.direita == None:
            if perc == self.raiz:
                self.raiz = perc.esquerda
            else:
                if filho_esquerdo:
                    pai.esquerda = perc.esquerda
                else:
                    pai.direita = perc.esquerda
                perc = None
        elif perc.esquerda == None:
            if self.raiz == perc:
                self.raiz = perc.direita
            else:
                if filho_esquerdo:
                    pai.esquerda = perc.direita
                else:
                    pai.direita = perc.direita
            perc = None
        else:
            novo, elemento = self.sucessor(perc)

            if perc == self.raiz:
                self.raiz = novo
            else:
                if filho_esquerdo:
                    pai.esquerda = novo
                else:
                    pai.direita = novo
            novo.esquerda = perc.esquerda
            perc = None
        return True

    def contador(self):
        return self.countSides(self.raiz)

    def countSides(self, raiz):
        CE = 0
        CD = 0
        if self.vazio():
            raise ValueError("Arvore vazia")
        perc = raiz
        if perc == None:
            return 'perc eh none'
        while perc.esquerda != None:
            perc = perc.esquerda
            CE += 1
        perc = raiz
        while perc.direita != None:
            perc = perc.direita
            CD += 1
        if CD > CE:
            return 'direita'
        else:
            return 'esquerda'

    # def returnH(self):
    # return self.getNivel()
    def get_nivel(self):
        perc = self.raiz
        temp = self.raiz
        ce = 1
        cd = 1
        perc = perc.direita
        temp = temp.esquerda
        while True:
            if self.countSides(perc) == 'direita' and perc.direita != None:
                perc = perc.direita
                cd += 1
            elif self.countSides(perc) == 'esquerda' and perc.esquerda != None:
                perc = perc.esquerda
                cd += 1
            if self.countSides(temp) == 'direita' and temp.direita != None:
                temp = temp.direita
                ce += 1
            elif self.countSides(temp) == 'esquerda' and temp.esquerda != None:
                temp = temp.esquerda
                ce += 1
            if ((temp.direita == None) and (temp.esquerda == None)) and ((perc.direita == None) and (perc.esquerda == None)):
                break
        if ce > cd:
            return ce + 1
        elif cd > ce:
            return cd + 1
        elif cd == ce:
            return cd + 1
        
    def get_maximo(self, raiz):
        if self.vazio():
            raise ValueError("A Árvore está vazia!")
        else:
            perc = raiz
            while perc.direita != None:
                perc = perc.direita
            return perc, perc.elemento

    def get_minimo(self, raiz):
        if self.vazio():
            raise ValueError("A Árvore está vazia!")
        else:
            perc = raiz
            while perc.esquerda != None:
                perc = perc.esquerda
            return perc, perc.elemento

    def get_tamanho(self):
        return self.__quantFolhas

    def sucessor(self, raiz):
        if raiz is None:
            raiz = self.raiz
        if raiz.direita != None:
            perc, elemento = self.get_minimo(raiz.direita)
            return perc, elemento

    def predecessor(self, raiz):
        if raiz is None:
            raiz = self.raiz
        if raiz.esquerda != None:
            perc, elemento = self.get_maximo(raiz.esquerda)
            return perc, elemento

    def buscar(self, elemento):
        perc = self.raiz
        if self.raiz.elemento == elemento:
            return self.raiz
        else:
            while True:
                if self.vazio():
                    raise ValueError("A lista está vazia!")
                elif elemento > perc.elemento and perc.direita != None:
                    if perc.direita.elemento != elemento:
                        perc = perc.direita
                    else:
                        return perc.direita
                elif elemento < perc.elemento and perc.esquerda != None:
                    if perc.esquerda.elemento != elemento:
                        perc = perc.esquerda
                    else:
                        return perc.esquerda
                else:
                    raise Exception("Elemento não encontrado na lista")

    def imprimirNo(self, no):
        if no != None:
            self.imprimirNo(no.esquerda)
            print(no, end=" ")
            self.imprimirNo(no.direita)

    def imprimir(self):
        self.imprimirNo(self.raiz)
        print()

    def vazio(self):
        if self.raiz is None:
            return True
        return False