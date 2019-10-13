from Lista import Lista

__dados = Lista()
__emprestimos = Lista()


def salvar_dados(contato):
    __dados.add_fim(contato)


def salvar_emprestimo(emprestimo):
    __emprestimos.add_fim(emprestimo)


def copia_dados():
    return __dados.copy()

def copia():
    return __emprestimos.copy()


def buscar_contato(login, senha):
    for contato in __dados:
        if contato.usuario == login and contato.senha == senha:
            return contato

def buscar_usuario(login):
    for contato in __dados:
        if contato.usuario == login:
            return contato


def remover_usuario(usuario, senha):
    for dado in __dados:
        if dado.usuario == usuario and dado.senha == senha:
            __dados.remover_elemento(dado)


def remover_emprestimo(item, usuario):
    for emprestimo in __emprestimos:
        if emprestimo.item == item:
            __emprestimos.remover_elemento(emprestimo)
    for dado in __dados:
        if dado.usuario == usuario:
            dado.devolver(item)
    