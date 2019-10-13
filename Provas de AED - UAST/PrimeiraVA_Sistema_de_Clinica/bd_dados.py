from Lista import Lista

__pacientes = Lista()
__consultas = Lista()


def salvar_paciente(paciente):
    __pacientes.add_fim(paciente)


def salvar_consultas(consulta):
    __consultas.add_fim(consulta)


def buscar_paciente(cpf):
    for paciente in __pacientes:
        if paciente.cpf == cpf:
            return paciente


def buscar_por_cod(cod):
    for consulta in __consultas:
        if consulta.cod == cod:
            return consulta


def copia_pacientes():
    return __pacientes.copy()


def copia_consultas():
    return __consultas.copy()
