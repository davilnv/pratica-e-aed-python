import menu, classes, bd_dados


def iniciar_paciente():
    while True:
        menu.menu_paciente()
        op = input("Escolha uma opção do Menu: ")
        if op == '0':
            break
        elif op == '1':
            cpf = input("Número do CPF: ")
            nome = input("Nome do paciente: ")
            sexo = input("Sexo: ")
            telefone = input("Telefone para contato: ")
            plano = input("Plano (Padrão, Normal, Especial): ")
            paciente = classes.Paciente(cpf, nome, sexo, telefone, plano)
            bd_dados.salvar_paciente(paciente)
            print("Paciente cadastrado com sucesso!")
        elif op == '2':
            cpf = input("CPF do Paciente: ")
            print(bd_dados.buscar_paciente(cpf))
        elif op == '3':
            pacientes = bd_dados.copia_pacientes()
            for pacien in pacientes:
                print(pacien)
        else:
            print("Opção inválida")
