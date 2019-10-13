class No():
    def __init__(self, elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.elemento)


class Arvore():
    def __init__(self):
        self.raiz = None
        self.__quantFolhas = 0

    def add(self, elemento):
        no = No(elemento)
        perc = self.raiz
        if self.empty():
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
                    raise Exception("Elemento já adicionado na árvore")
        self.__quantFolhas += 1

    def getTamanho(self):
        return self.__quantFolhas

    def imprimirNo(self, no):
        if no != None:
            self.imprimirNo(no.esquerda)
            print(no, end=" ")
            self.imprimirNo(no.direita)

    def imprimir(self):
        self.imprimirNo(self.raiz)
        print()

    def _buscar(self,elemento,pai, perc):
        if perc !=None:
            if perc.elemento == elemento:
                return pai,  perc
            elif elemento < perc.elemento:
                return self._buscar(elemento, perc, perc.esquerda)
            else:
                return self._buscar(elemento, perc, perc.direita)
        else:
            raise RecursionError('Erro de recursão')

    def buscar(self,elemento):
        return self._buscar(elemento, self.raiz, self.raiz)

    def get_min(self, raiz):
        if self.empty():
            raise ValueError("Arvore vazia")
        perc = raiz
        while perc.esquerda != None:
            perc = perc.esquerda
        return perc

    def get_max(self, raiz):
        if self.empty():
            raise ValueError("Arvore vazia")
        perc = raiz
        while perc.direita != None:
            perc = perc.direita
        return perc

    def sucessor(self, raiz):
        if raiz.direita != None:
            return self.get_min(raiz.direita)

    def predecessor(self, raiz):
        if raiz.esquerda != None:
            return self.get_max(raiz.esquerda)

    def empty(self):
        if self.raiz == None:
            return True
        return False

    def getleaf(self, pai):
        if pai.direita != None or pai.esquerda != None:
            return True
        else:
            return False

    def isfilhos(self, pai):
        if pai.esquerda != None and pai.direita != None:
            return True
        else:
            return False

    def Remover(self, elemento):
        if self.empty():
            raise ValueError("Arvore vazia")
        perc, pai = self.raiz, self.raiz
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
                    perc = None
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
            novo = self.sucessor(perc)

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
        CE, CD = 0, 0
        if self.empty():
            raise ValueError("Arvore vazia")
        perc = raiz
        if perc == None:
            return 'perc eh none'
        while perc.esquerda != None:
            perc, CE = perc.esquerda, CE+1
        perc = raiz
        while perc.direita != None:
            perc, CD = perc.direita, CD+1
        if CD > CE:
            return 'right'
        else:
            return 'left'

    def ReturnNivel(self):
        return self.getNivel(self.raiz)

    def getNivel(self, posicao):
        perc = posicao
        temp = posicao
        ce, cd = 1, 1
        perc = perc.direita
        temp = temp.esquerda
        while True:
            if self.countSides(perc) == 'right' and perc.direita != None:
                perc,cd = perc.direita, cd+1
            elif self.countSides(perc) == 'left' and perc.esquerda != None:
                perc = perc.esquerda, cd+1
            if self.countSides(temp) == 'right'and temp.direita != None:
                temp, ce = temp.direita, ce+1
            elif self.countSides(temp) == 'left' and temp.esquerda != None:
                temp = temp.esquerda, ce+1
            if ((temp.direita == None) and (temp.esquerda == None)) and ((perc.direita == None) and (perc.esquerda == None)):
                break
        if ce > cd:
            return ce+1
        elif cd > ce:
            return cd+1
        elif cd == ce:
            return cd+1

    def peganivel(self, posicao):
        perc, temp = posicao, posicao
        ce, cd = 1, 1
        perc, temp = perc.direita, temp.esquerda
        while True:
            if self.countSides(perc) == 'right' and perc.direita != None:
                perc, cd = perc.direita, cd+1
            elif self.countSides(perc) == 'left' and perc.esquerda != None:
                perc, cd = perc.esquerda, cd+1
            if self.countSides(temp) == 'right'and temp.direita != None:
                temp, ce = temp.direita, ce+1
            elif self.countSides(temp) == 'left' and temp.esquerda != None:
                temp, ce = temp.esquerda, ce+1

            if ((temp!= None) and (perc != None)):
                if ((temp.direita == None) and (temp.esquerda == None)) and ((perc.direita == None) and (perc.esquerda == None)):
                    break
            elif ((temp == None) and (perc == None)):
                break
            elif ((perc == None) and (temp != None)):
                if temp.direita == None and temp.esquerda == None:
                    break
            elif ((temp == None) and (perc != None)):
                if perc.direita == None and perc.esquerda == None:
                    break
        return ce, cd

    def fatorBalanceamento(self, elemento):
        hl, hr = self.peganivel(elemento)
        balanceamento = self.getBalanceamento(hl, hr)
        if balanceamento >= 2:
            return 2
        elif balanceamento == 1:
            return 1
        elif balanceamento <= -2:
            return -2
        elif balanceamento == -1:
            return -1
        else:
            return 0

    def getBalanceamento(self, hl, hr):
        return hl - hr

    def LL(self, posicao):
        pai, side, perc = self.buscar(posicao)
        if self.fatorBalanceamento(pai) == 2 and self.fatorBalanceamento(perc) == 1:
            paiTemp = pai
            paiTemp.esquerda = self.predecessor(pai)
            pai = perc
            pai.direita = paiTemp
            pai.esquerda = perc.esquerda
            self.raiz = pai

    def RR(self, posicao):
        pai, side, perc = self.buscar(posicao)
        if self.fatorBalanceamento(pai) == -2 and self.fatorBalanceamento(perc) == -1:
            pai.direita = perc.esquerda
            perc.esquerda = pai
            self.raiz = perc

    def LR(self, posicao):
        pai, side, perc = self.buscar(posicao)
        if self.fatorBalanceamento(pai) == 2 and (pai.esquerda == perc):
            perc1 = perc.direita
            perc.direita = perc1.esquerda
            perc1.esquerda = perc
            pai.esquerda = perc1.direita
            perc1.direita = pai
            self.raiz = perc1

    def RL(self, posicao):
        pai, side, perc = self.buscar(posicao)
        if self.fatorBalanceamento(pai) == -2 and (pai.direita == perc):
            perc1 = perc.esquerda
            perc.esquerda = perc1.direita
            perc1.direita = perc
            pai.direita = perc1.esquerda
            perc1.esquerda = pai
            self.raiz = perc1

    def getElementByNivel(self, nivel):
        if self.empty():
            raise ValueError("Arvore vazia")
        perc, temp = self.raiz, self.raiz
        ce, cd, perc, temp = 1, 1, perc.direita, temp.esquerda
        if nivel == 0:
            print(self.raiz)
        else:
            while True:
                paiRight, paiLeft = perc, temp
                if (self.countSides(perc)) == 'right' and (perc.direita != None):
                    perc, cd = perc.direita, cd+1
                elif (self.countSides(perc)) == 'left' and (perc.esquerda != None):
                    perc, cd = perc.esquerda, cd+1
                if (self.countSides(temp)) == 'right' and (temp.direita != None):
                    temp, ce = temp.direita, ce+1
                elif (self.countSides(temp)) == 'left' and (temp.esquerda != None):
                    temp, ce = temp.esquerda, ce+1

                if (ce == nivel) and (cd == nivel):
                    return paiLeft.elemento, paiRight.elemento
                break


arvore = Arvore()
arvore.add(10)
arvore.add(20)
arvore.add(30)
arvore.add(5)
print(arvore.somar(arvore.raiz))
