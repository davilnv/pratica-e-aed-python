import menu, controlador_paciente, controlador_consulta

while True:
    menu.menu_principal()
    op = input("Esolha uma opção do Menu: ")
    if op == '0':
        break
    elif op == '1':
        controlador_paciente.iniciar_paciente()
    elif op == '2':
        controlador_consulta.iniciar_consulta()
    else:
        print("Opção inválida")
