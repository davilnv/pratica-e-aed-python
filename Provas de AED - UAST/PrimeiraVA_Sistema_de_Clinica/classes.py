class Paciente:
    def __init__(self, cpf, nome, sexo, telefone, plano):
        self.cpf = cpf
        self.nome = nome
        self.sexo = sexo
        self.telefone = telefone
        self.plano = plano

    def __str__(self):
        return f'Nome: {self.nome} - CPF: {self.cpf} - Plano: {self.plano}'


class Consulta:
    def __init__(self, cod, crm, nome_medico, cpf_paciente, valor, desconto):
        self.cod = cod
        self.crm = crm
        self.nome_medico = nome_medico
        self.cpf_paciente = cpf_paciente
        self.valor = valor
        self.desconto = desconto

    def __str__(self):
        return f'Código: {self.cod} - Doutor(a) {self.nome_medico} - CRM: {self.crm} - CPF do paciente: ' \
            f'{self.cpf_paciente} - Valor da consulta: {self.valor}'
