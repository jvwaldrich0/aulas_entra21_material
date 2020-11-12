from datetime import date
from banco import Conta

class Pessoa:
    def __init__(self, nome: str, cpf, dia: int, mes: int, ano: int, motorista: bool = False,
                 habilitacao: bool = False, conta: bool = False, id_conta: Conta = None):
        self.firstname = nome.upper()
        if len(cpf) != 11:
            raise AttributeError('CPF Inválido')
        else:
            try:
                int(cpf)
            except ValueError:
                raise AttributeError('CPF Inválido')
            self.cpf = (f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}.{cpf[9:11]}')
        self.idade = self.calcular_idade(dia, mes, ano)
        self.nascimento = date(day=dia, month=mes, year=ano)
        if motorista and habilitacao:
            self.habilitacao = True
            self.motorista = True
        else:
            self.motorista = False
            self.habilitacao = habilitacao
        self.conta = conta
        self.id_conta = id_conta

    def __str__(self):
        return self.firstname

    @staticmethod
    def calcular_idade(dia, mes, ano) -> int:
        born = date(day=dia, month=mes, year=ano)
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

