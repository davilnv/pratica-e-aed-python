from src import menu, controlador_agenda

while True:
    menu.menu_principal()
    op = input('Escolha uma opção do MENU: ')
    if op == '0':
        break
    elif op == '1':
        controlador_agenda.cadastrar()
    elif op == '2':
        controlador_agenda.listar_contatos()
    elif op == '3':
        controlador_agenda.buscar_contato()
    elif op == '4':
        controlador_agenda.editar_contato()
    elif op == '5':
        controlador_agenda.apagar_contato()
    else:
        print("Opção inválida! Tente novamente")
