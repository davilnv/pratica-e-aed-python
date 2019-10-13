import classes, bd_dados, menu

def iniciar_controle():
    while True:
        menu.menu_cadastro()
        op = input("Escolha uma opção: ")
        if op == '0':
            break
        elif op == '1':
            usuario = input("Usuario(Nickname): ")
            busca = bd_dados.buscar_usuario(usuario)
            if not busca:
                senha = input("Senha de Acesso: ")
                nome = input("Nome Completo: ")
                data_nascimento = input("Data de Nascimento (DD/MM/AA): ")
                email = input("Email: ")
                contato = input("Número para Contato: ")
                amigo = classes.Amigo(usuario, senha, nome, data_nascimento, email, contato)
                bd_dados.salvar_dados(amigo)
                print()
            else:
                print("Nome de usuário já cadastrado")
        else:
            print("Opção Inválida!")
