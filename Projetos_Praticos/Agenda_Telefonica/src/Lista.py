import copy


class No:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None
        self.anterior = None


class Lista:
    def __init__(self, tipo=None):
        self.inicio = None
        self.fim = None
        self.__tamanho = 0
        self.tipo = tipo

    def validar_tipo(self, elemento):
        if self.tipo is not None:
            if type(elemento) == self.tipo:
                return True
            return False
        return True

    def vazia(self):
        if self.inicio is None:
            return True
        return False

    def add_inicio(self, elemento):
        if self.validar_tipo(elemento):
            no = No(elemento)
            if self.vazia(): # self.inicio is None:
                self.inicio = no
                self.fim = no
            else:
                no.proximo = self.inicio
                self.inicio.anterior = no
                no.anterior = None
                self.inicio = no
            self.__tamanho += 1
        else:
            raise TypeError("Tipo de elemento adicionado não é o mesmo da lista")

    def add_fim(self, elemento):
        if self.validar_tipo(elemento):
            no = No(elemento)
            if self.vazia(): # self.inicio is None:
                self.inicio = no
                self.fim = no
            else:
                self.fim.proximo = no
                no.anterior = self.fim
                no.proximo = None
                self.fim = no
                """
                perc = self.inicio
                while perc.proximo is not None:
                    perc = perc.proximo
                perc.proximo = no
                no.anterior = perc
                self.fim = no
                """
            self.__tamanho += 1
        else:
            raise TypeError("Tipo de elemento adicionado não é o mesmo da lista")

    def add_index(self, i, elemento):
        metade = int(self.__tamanho / 2)
        if self.validar_tipo(elemento):
            if i > self.__tamanho:
                raise TypeError("Posição de memória inválida!")
            if i == self.__tamanho:
                self.add_fim(elemento)
            elif i == 0:
                self.add_inicio(elemento)
            else:
                if i <= metade:
                    no = No(elemento)
                    perc = self.inicio
                    cont = 0
                    while cont < i - 1:
                        perc = perc.proximo
                        cont += 1
                    no.proximo = perc.proximo
                    perc.proximo.anterior = no
                    perc.proximo = no
                    no.anterior = perc
                else:
                    no = No(elemento)
                    perc = self.fim
                    cont = self.__tamanho
                    while cont > i:
                        perc = perc.anterior
                        cont -= 1
                    no.proximo = perc.proximo
                    perc.proximo.anterior = no
                    perc.proximo = no
                    no.anterior = perc
                self.__tamanho += 1
        else:
            raise TypeError("Tipo de elemento adicionado não é o mesmo da lista")

    def remover_inicio(self):
        if self.vazia(): #self.inicio is None:
            raise TypeError("Lista está vazia!")
        elif self.__tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        self.__tamanho -= 1

    def remover_fim(self):
        if self.vazia(): #self.inicio is None:
            raise TypeError("Lista está vazia!")
        elif self.__tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        self.__tamanho -= 1

    def remover_meio(self, i):
        if self.vazia(): #self.inicio is None:
            raise TypeError("Lista está vazia!")
        elif i == 0:
            self.remover_inicio()
        elif i == self.__tamanho - 1:
            self.remover_fim()
        else:
            perc = self.inicio
            cont = 0
            while cont < i -1:
                perc = perc.proximo
                cont += 1
            aux = perc.proximo
            perc.proximo = aux.proximo
            aux.proximo.anterior = perc
            aux = None
            self.__tamanho -= 1

    def remover_elemento(self, elemento):
        if self.__tamanho == 0:
            return None
        perc = self.inicio
        cont = 0
        while perc.elemento != elemento:
            perc = perc.proximo
            cont += 1
        self.remover_meio(cont)

    def copy(self):
        return copy.copy(self)

    def sobrescrever(self, index, elemento):
        perc = self.inicio
        cont = 0
        while cont != index:
            perc = perc.proximo
            cont += 1
        perc.elemento = elemento

    def get_tamanho(self):
        return self.__tamanho

    def get_index(self, i):
        perc = self.inicio
        cont = 0
        while cont < self.__tamanho:
            if cont == i:
                return perc.elemento
            perc = perc.proximo
            cont += 1

    def __str__(self):
        valor = '['
        if self.inicio is not None:
            perc = self.inicio
            valor += str(perc.elemento)
            while perc.proximo is not None:
                perc = perc.proximo
                valor += ', '
                valor += str(perc.elemento)
        valor += ']'
        return valor

    def __len__(self):
        return self.get_tamanho()

    def __getitem__(self, item):
        if item >= self.__tamanho:
            raise StopIteration
        return self.get_index(item)

    def __setitem__(self, key, value):
        return self.sobrescrever(key, value)
