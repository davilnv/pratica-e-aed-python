import menu, controlador_cadastro, controlador_emprestimo, controlador_admin

while True:
    menu.menu_principal()
    op = input("Escolha uma opção: ")
    if op == '0':
        print("Saindo...")
        break
    elif op == '1':
        controlador_cadastro.iniciar_controle()
    elif op == '2':
        controlador_emprestimo.iniciar_emprestimo()
    elif op == '3':
        controlador_admin.iniciar_admin()
    else:
        print("Opção inválida!")
