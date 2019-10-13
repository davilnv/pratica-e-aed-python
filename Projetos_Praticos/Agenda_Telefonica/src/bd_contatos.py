from src.Lista import Lista

dados = Lista()


def salvar_contato(contato):
    dados.add_fim(contato)


def listar():
    if dados is not None:
        for contato in dados:
            contato.get_dados_lista()
    else:
        print('A lista telefônica está vazia!')


def buscar(email):
    for contato in dados:
        if contato.email == email:
            return contato
    else:
        return None


def apagar(email):
    for contato in dados:
        if contato.email == email:
            dados.remover_elemento(contato)