import menu, classes, bd_dados


def iniciar_consulta():
    while True:
        menu.menu_consulta()
        op = input("Escolha uma opção do Menu: ")
        if op == '0':
            break
        elif op == '1':
            cod = input("Código da Consulta: ")
            crm = input("CRM do Médico: ")
            nome_medico = input("Nome do médico: ")
            cpf_paciente = input("CPF do Paciente: ")
            valor = input("Valor da Consulta: ")
            desconto = input("Desconto na consulta (10, 20, 30): ")
            consulta = classes.Consulta(cod, crm, nome_medico, cpf_paciente, valor, desconto)
            bd_dados.salvar_consultas(consulta)
            print("Consulta cadastrada com sucesso!")
        elif op == '2':
            cod = input("Código da consulta que deseja buscar: ")
            print(bd_dados.buscar_por_cod(cod))
        elif op == '3':
            consultas = bd_dados.copia_consultas()
            for consul in consultas:
                print(consul)
        elif op == '4':
            cpf = input("CPF para Listar consultas: ")
            consultas_cpf = bd_dados.copia_consultas().listar_consultas_cpf(cpf)
            for c in consultas_cpf:
                print(c)
        elif op == '5':
            crm = input("CRM do Médico para Listar Consultas: ")
            consultas_crm = bd_dados.copia_consultas().listar_consultas_crm(crm)
            for con in consultas_crm:
                print(con)
        else:
            print("Opção inválida!")
