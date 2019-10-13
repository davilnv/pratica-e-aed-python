import bd_dados, menu, classes

def iniciar_emprestimo():
    print("---- Tela de Empréstimo ----")
    login = input("Usuário de Acesso: ")
    senha = input("Senha de Acesso: ")
    contato = bd_dados.buscar_contato(login, senha)
    if contato is None:
        print("Dados não encontrados!")
    else:
        while True:
            menu.menu_emprestimo()
            op = input("Escolha uma opção: ")
            if op == '0':
                print("Saindo...")
                break
            elif op == '1':
                item = input("Item que será emprestado: ")
                data_emprestimo = input("Data do empréstimo: ")
                emprestimo = classes.Emprestimo(item, data_emprestimo, contato)
                bd_dados.salvar_emprestimo(emprestimo)
                contato.emprestimos.add_fim(emprestimo)
            elif op == '2':
                for item in contato.emprestimos:
                    print(item.listar())
            elif op == '3':
                item_emprestado = input("Qual o item que deseja devolver? ")
                usuario = input("Usuario para confirmar devolução: ")
                bd_dados.remover_emprestimo(item_emprestado, usuario)
            else:
                print("Opção Inválida!")
