class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, pais):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.pais = pais


class Contato:
    def __init__(self, email, nome, telefone, celular):
        self.email = email
        self.nome = nome
        self.telefone = telefone
        self.celular = celular
        self.endereco = None

    def get_dados_lista(self):
        print(f'Nome: {self.nome}, Email: {self.email}')

    def mostrar_contato(self):
        return f'-------------------------\n' \
            f'Nome: {self.nome}\n' \
            f'Email: {self.email}\n' \
            f'Telefone: {self.telefone}\n' \
            f'Número do celular: {self.celular}'

    def mostrar_endereco(self):
        return  \
            f'Endereço: {self.endereco.rua}, {self.endereco.numero}\n' \
            f'          {self.endereco.bairro}, {self.endereco.cidade}\n' \
            f'          {self.endereco.estado}, {self.endereco.pais}\n'

    def salvar_endereco(self):
        rua = input('Rua: ')
        numero = input('Número: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        estado = input('Estado: ')
        pais = input('Pais: ')
        self.endereco = Endereco(rua, numero, bairro, cidade, estado, pais)
