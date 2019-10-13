from src import classes, bd_contatos, menu


def cadastrar():
    email = input('Email: ')
    nome = input('Nome: ')
    telefone = input('Telefone Fixo: ')
    celular = input('Número do Celular: ')
    contato = classes.Contato(email, nome, telefone, celular)
    print('Deseja salvar o endereço do contato?')
    op = input('Opção [S/N]: ')
    if op in 'Ss':
        contato.salvar_endereco()
        print('Contato cadastrado!')
    else:
        print('Contato cadastrado sem endereço')
    bd_contatos.salvar_contato(contato)
    print()


def listar_contatos():
    print('------ LISTA DE CONTATOS ------')
    bd_contatos.listar()
    print()


def buscar_contato():
    email = input('Digite o email do contato que deseja procurar: ')
    contato = bd_contatos.buscar(email)
    if contato is not None:
        if contato.endereco is not None:
            print(contato.mostrar_contato())
            print(contato.mostrar_endereco())
        else:
            print(contato.mostrar_contato())
    else:
        print('Contato não encontrado!')
    print()


def editar_contato():
    menu.menu_edicao()
    email = input('Qual o email do contato que deseja alterar? ')
    contato = bd_contatos.buscar(email)

    def alterar_endereco():
        contato.endereco.rua = input('Rua: ')
        contato.endereco.numero = input('Número: ')
        contato.endereco.bairro = input('Bairro: ')
        contato.endereco.cidade = input('Cidade: ')
        contato.endereco.estado = input('Estado: ')
        contato.endereco.pais = input('País: ')

    if contato is not None:
        while True:
            op = input('Escolha uma opção: ')
            if op == '0':
                break
            elif op == '1':
                contato.nome = input('Nome: ')
            elif op == '2':
                contato.telefone = input('Telefone: ')
            elif op == '3':
                contato.celular = input('Número do celular: ')
            elif op == '4':
                print()
                menu.menu_edicao_endereco()

                while True:
                    opc = input('Escolha uma opção: ')
                    if opc == '0':
                        break
                    elif opc == '1':
                        contato.endereco.rua = input('Rua: ')
                    elif opc == '2':
                        contato.endereco.numero = input('Número: ')
                    elif opc == '3':
                        contato.endereco.bairro = input('Bairro: ')
                    elif opc == '4':
                        contato.endereco.cidade = input('Cidade: ')
                    elif opc == '5':
                        contato.endereco.estado = input('Estado: ')
                    elif opc == '6':
                        contato.endereco.pais = input('País: ')
                    elif opc == '7':
                        alterar_endereco()
                    else:
                        print('Opção inválida')
            elif op == '5':
                contato.nome = input('Nome: ')
                contato.telefone = input('Telefone: ')
                contato.celular = input('Número do celular: ')
                if contato.endereco is not None:
                    alterar_endereco()
            else:
                print('Opção inválida!')

    else:
        print('Contato não encontrado!')


def apagar_contato():
    email = input('Digite o email do contato que deseja apagar: ')
    bd_contatos.apagar(email)
