import menu, bd_dados, classes

def iniciar_admin():
    login = input("Usuário de Acesso ADMIN: ")
    senha = input("Senha de Acesso ADMIN: ")
    admin = classes.Admin()
    if admin.usuario == login and admin.senha == senha:
        while True:
            menu.menu_admin()
            op = input("Escolher uma opção: ")
            if op == '0':
                break
            elif op == '1':
                emprestimos = bd_dados.copia()
                for emprestimo in emprestimos:
                    print(emprestimo.listar())
            elif op == '2':
                login_busca = input('Usuário para buscar: ')
                dado = bd_dados.buscar_usuario(login_busca)
                for item in dado.emprestimos:
                    print(item.listar())
            elif op == '3':
                usuarios = bd_dados.copia_dados()
                for usuario in usuarios:
                    print(f"Nome: {usuario.nome} / Número de Contato: {usuario.numero_contato}")
            elif op == '4':
                usuario_busca = input('Usuário para remover: ')
                usuario_senha = input('Senha do usuário para remover: ')
                bd_dados.remover_usuario(usuario_busca, usuario_senha)
            elif op == '5':
                op = input("Tem certeza que quer modificar o ADMIN? [S/N]: ")
                if op in "Ss":
                    admin.nome = input("Nome do novo ADMIN: ")
                    admin.usuario = input("Usuário do novo ADMIN: ")
                    admin.senha = input("Senha de Acesso do novo ADMIN: ")                   
            else:
                print("Opção Inválida!")
    else:
        print("Acesso negado!")
