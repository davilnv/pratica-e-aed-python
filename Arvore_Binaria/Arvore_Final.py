class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.esquerda = None
        self.direita = None


class Arvore:
    def __init__(self):
        self.raiz = None
        self.__tamanho = 0
        self.__soma = 0
        self.__listaE = []
        self.__elementosNo = 0

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
                    if no.elemento < no_atual.elemento:
                        no_atual = no_atual.esquerda
                    else:
                        no_atual = no_atual.direita
                else:
                    if no.elemento < no_pai.elemento:
                        no_pai.esquerda = no
                    else:
                        no_pai.direita = no
                    break
        self.__tamanho += 1

    def remover(self, elemento):
        if self.vazia():
            raise ValueError("Arvore vazia")
        no_pai, no_atual = self.raiz, self.raiz
        filho_esquerdo = True
        while no_atual.elemento != elemento:
            no_pai = no_atual
            if elemento < no_atual.elemento:
                no_atual = no_atual.esquerda
                filho_esquerdo = True
            else:
                no_atual = no_atual.direita
                filho_esquerdo = False
            if no_atual is None:
                return False
        # 1 Caso
        if no_atual.esquerda is None and no_atual.direita is None:
            if no_atual == self.raiz:
                self.raiz = None
            else:
                if filho_esquerdo:
                    no_pai.esquerda = None
                else:
                    no_pai.direita = None
        # 2 Caso
        elif no_atual.direita is None:
            if self.raiz == no_atual:
                self.raiz = no_atual.esquerda
            else:
                if filho_esquerdo:
                    no_pai.esquerda = no_atual.esquerda
                    no_atual = None
                else:
                    no_pai.direita = no_atual.esquerda
                    no_atual = None
        elif no_atual.esquerda is None:
            if self.raiz == no_atual:
                self.raiz = no_atual.direita
            else:
                if filho_esquerdo:
                    no_pai.esquerda = no_atual.direita
                    no_atual = None
                else:
                    no_pai.direita = no_atual.direita
                    no_atual = None
        # 3 Caso
        else:
            no_elemento, novo_no = self.sucessor(no_atual)
            if no_atual == self.raiz:
                self.raiz = novo_no
            else:
                if filho_esquerdo:
                    no_pai.esquerda = novo_no
                else:
                    no_pai.direita = novo_no
            novo_no.esquerda = no_atual.esquerda
            no_atual = None
        return True

    def _buscar(self, elemento, no_pai, no_atual):
        if no_atual is not None:
            if no_atual.elemento == elemento:
                return no_pai, no_atual
            elif elemento < no_atual.elemento:
                return self._buscar(elemento, no_atual, no_atual.esquerda)
            else:
                return self._buscar(elemento, no_atual, no_atual.direita)
        else:
            raise RecursionError("Erro de recursão")

    def buscar(self, elemento):
        return self._buscar(elemento, self.raiz, self.raiz)

    def _buscar_elemento(self, elemento, no_atual):
        if no_atual is not None:
            if no_atual.elemento == elemento:
                return no_atual.elemento
            elif elemento < no_atual.elemento:
                return self._buscar_elemento(elemento, no_atual.esquerda)
            else:
                return self._buscar_elemento(elemento, no_atual.direita)
        else:
            raise RecursionError("Erro de recursão")

    def buscar_elemento(self, elemento):
        return self._buscar_elemento(elemento, self.raiz)

    def vazia(self):
        if self.raiz is None:
            return True
        return False

    def _mostrar_no(self, no):
        if no is not None:
            self._mostrar_no(no.esquerda)
            print(no.elemento, end=" ")
            self._mostrar_no(no.direita)

    def mostrar(self):
        self._mostrar_no(self.raiz)
        print()

    def somar(self, no):
        if no is not None:
            self.somar(no.esquerda)
            self.__soma += no.elemento
            self.somar(no.direita)

    def somar_elementos(self):
        self.somar(self.raiz)
        return self.__soma

    # Não está retornando o valor certo
    def nivel_elemento(self, elemento):
        no = No(elemento)
        nivel = 0
        if self.vazia():
            return "A árvore está vazia!"
        else:
            no_pai = None
            no_atual = self.raiz
            while True:
                no_pai = no_atual
                if elemento == no_atual.elemento:
                    break
                if elemento < no_atual.elemento:
                    no_atual = no_atual.esquerda
                    nivel += 1
                else:
                    no_atual = no_atual.direita
                    nivel += 1
        return nivel

    def verificar_nivel(self, nivel, raiz):
        if raiz is not None:
            self.verificar_nivel(nivel, raiz.esquerda)
            if self.nivel_elemento(raiz.elemento) == nivel:
                return self.__listaE.append(raiz.elemento)
            self.verificar_nivel(nivel, raiz.direita)

    def elementosCada_nivel(self, nivel):
        self.verificar_nivel(nivel, self.raiz)
        return self.__listaE

    def elementos_no(self, raiz):
        if raiz is not None:
            self.elementos_no(raiz.esquerda)
            self.__elementosNo += 1
            self.elementos_no(raiz.direita)

    def totElementos_no(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        self.elementos_no(raiz)
        return self.__elementosNo

    def fator_balanceamento(self, raiz):
        if raiz.esquerda is not None or raiz.direita is not None:
            nivelE = self.pegar_nivel(raiz.esquerda)
            nivelD = self.pegar_nivel(raiz.direita)
            return nivelE - nivelD
        else:
            return 0

    def pegar_nivel(self, raiz):
        percE = raiz
        contE = 1
        while True:
            if percE is None:
                contE -= 1
                break
            elif percE.esquerda is None and percE.direita is None:
                break
            if self.maior_lado(percE) == "E" and percE.esquerda is not None:
                percE = percE.esquerda
                contE += 1
            elif self.maior_lado(percE) == "D" and percE.direita is not None:
                percE = percE.direita
                contE += 1
        percD = raiz
        contD = 1
        while True:
            if percD is None:
                contD -= 1
                break
            elif percD.esquerda is None and percD.direita is None:
                break
            if self.maior_lado(percD) == "E" and percD.esquerda is not None:
                percD = percD.esquerda
                contD += 1
            elif self.maior_lado(percD) == "D" and percD.direita is not None:
                percD = percD.direita
                contD += 1
        if contD > contE:
            return contD
        elif contD < contE:
            return contE
        elif contD == contE:
            return contD

    def RSE(self, elemento):
        pai, perc = self.buscar(elemento)
        pai_do_pai, paiT = self.buscar(pai.elemento)
        fator1 = self.fator_balanceamento(pai)
        fator2 = self.fator_balanceamento(perc)
        if fator1 == -2 and fator2 == -1:
            if pai == self.raiz:
                perc.esquerda = pai
                pai.direita = None
                pai = perc
                self.raiz = pai
            elif pai_do_pai.esquerda == pai:
                pai_do_pai.esquerda = pai.direita
                perc.esquerda = pai
                pai.direita = None
                pai = perc
            elif pai_do_pai.direita == pai:
                pai_do_pai.direita = pai.direita
                perc.esquerda = pai
                pai.direita = None
                pai = perc

    def RSD(self, elemento):
        pai, perc = self.buscar(elemento)
        pai_do_pai, paiT = self.buscar(pai.elemento)
        fator1 = self.fator_balanceamento(pai)
        fator2 = self.fator_balanceamento(perc)
        if fator1 == 2 and fator2 == 1:
            if pai == self.raiz:
                perc.direita = pai
                pai.esquerda = None
                pai = perc
                self.raiz = pai
            elif pai_do_pai.esquerda == pai:
                pai_do_pai.esquerda = pai.esquerda
                perc.direita = pai
                pai.esquerda = None
                pai = perc
            elif pai_do_pai.direita == pai:
                pai_do_pai.direita = pai.esquerda
                perc.direita = pai
                pai.esquerda = None
                pai = perc

    def RDE(self, elemento):
        pai, perc = self.buscar(elemento)
        pai_do_pai, paiT = self.buscar(pai.elemento)
        fator1 = self.fator_balanceamento(pai)
        fator2 = self.fator_balanceamento(perc)
        if fator1 == -2 and fator2 == 1:
            percF = perc.esquerda
            percF.direita = perc
            perc.esquerda = None
            pai.direita = percF
            perc = percF
        if fator1 == -2:
            if pai == self.raiz:
                perc.esquerda = pai
                pai.direita = None
                pai = perc
                self.raiz = pai
            elif pai_do_pai.esquerda == pai:
                pai_do_pai.esquerda = pai.direita
                perc.esquerda = pai
                pai.direita = None
                pai = perc
            elif pai_do_pai.direita == pai:
                pai_do_pai.direita = pai.direita
                perc.esquerda = pai
                pai.direita = None
                pai = perc

    def RDD(self, elemento):
        pai, perc = self.buscar(elemento)
        pai_do_pai, paiT = self.buscar(pai.elemento)
        fator1 = self.fator_balanceamento(pai)
        fator2 = self.fator_balanceamento(perc)
        if fator1 == 2 and fator2 == -1:
            percF = perc.direita
            percF.esquerda = perc
            perc.direita = None
            pai.esquerda = percF
            perc = percF
        if fator1 == -2:
            if pai == self.raiz:
                perc.direita = pai
                pai.esquerda = None
                pai = perc
                self.raiz = pai
            elif pai_do_pai.esquerda == pai:
                pai_do_pai.esquerda = pai.esquerda
                perc.direita = pai
                pai.esquerda = None
                pai = perc
            elif pai_do_pai.direita == pai:
                pai_do_pai.direita = pai.esquerda
                perc.direita = pai
                pai.esquerda = None
                pai = perc

    def balanceamento(self, elemento):
        pai, perc = self.buscar(elemento)
        fator1 = self.fator_balanceamento(pai)
        fator2 = self.fator_balanceamento(perc)
        if fator1 == -2 and fator2 == -1:
            self.RSE(elemento)
        elif fator1 == 2 and fator2 == 1:
            self.RSD(elemento)
        elif fator1 == -2 and fator2 == 1:
            self.RDE(elemento)
        elif fator1 == 2 and fator2 == -1:
            self.RDD(elemento)

    def altura_arvore(self):
        return self.get_nivel(self.raiz)

    def maior_lado(self, raiz):
        percD = raiz
        percE = raiz
        nivelDireito = 0
        nivelEquerdo = 0
        while percD.direita is not None:
            percD = percD.direita
            nivelDireito += 1
        while percE.esquerda is not None:
            percE = percE.esquerda
            nivelEquerdo += 1
        if nivelDireito > nivelEquerdo:
            return "D"
        elif nivelDireito < nivelEquerdo:
            return "E"
        elif nivelDireito == nivelEquerdo:
            return "D"

    def get_nivel(self, raiz):
        percE = raiz
        contE = 1
        while True:
            if percE is None or (percE.esquerda is None and percE.direita is None):
                break
            if self.maior_lado(percE) == "E" and percE.esquerda is not None:
                percE = percE.esquerda
                contE += 1
            elif self.maior_lado(percE) == "D" and percE.direita is not None:
                percE = percE.direita
                contE += 1
        percD = raiz
        contD = 1
        while True:
            if percD is None or (percD.esquerda is None and percD.direita is None):
                break
            if self.maior_lado(percD) == "E" and percD.esquerda is not None:
                percD = percD.esquerda
                contD += 1
            elif self.maior_lado(percD) == "D" and percD.direita is not None:
                percD = percD.direita
                contD += 1
        if contD > contE:
            return contD
        elif contD < contE:
            return contE
        elif contD == contE:
            return contD

    def get_raiz(self):
        return self.raiz

    def get_tamanho(self):
        return self.__tamanho

    def get_minimo(self, raiz):
        if self.vazia():
            raise ValueError("A árvore está vazia!")
        else:
            no_atual = raiz
            while no_atual.esquerda is not None:
                no_atual = no_atual.esquerda
            return no_atual.elemento, no_atual

    def get_maximo(self, raiz):
        if self.vazia():
            raise ValueError("A árvore está vazia!")
        else:
            no_atual = raiz
            while no_atual.direita is not None:
                no_atual = no_atual.direita
            return no_atual.elemento, no_atual

    def predecessor(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        if raiz.esquerda is not None:
            return self.get_maximo(raiz.esquerda)

    def sucessor(self, raiz=None):
        if raiz is None:
            raiz = self.raiz
        if raiz.direita is not None:
            return self.get_minimo(raiz.direita)
