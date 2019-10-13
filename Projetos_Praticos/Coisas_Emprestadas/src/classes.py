import Lista

class Amigo:
    def __init__(self, usuario, senha, nome, data_nascimento, email, numero_contato):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email
        self.numero_contato = numero_contato
        self.emprestimos = Lista.Lista()

    def devolver(self, item):
        for emprestimo in self.emprestimos:
            if emprestimo.item == item:
                self.emprestimos.remover_elemento(emprestimo)


class Emprestimo:
    def __init__(self, item, data_emprestimo, contato):
        self.item = item
        self.data_emprestimo = data_emprestimo
        self.contato = contato
    
    def listar(self):
        return f"--------------------------------------------------\n" \
            f"Item Emprestado: {self.item}\n" \
            f"Data do Empréstimo: {self.data_emprestimo}\n" \
            f"Contato: {self.contato.nome}, {self.contato.email}, {self.contato.numero_contato}\n"

class Admin:
    def __init__(self):
        self.nome = "Davi"
        self.usuario = "jackhemming"
        self.senha = "12345678"

