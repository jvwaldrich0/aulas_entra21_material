from datetime import date


class Pessoa:
    """"
    Classe Pessoa tem como objetivo criar uma classe geral para pessoas
    """
    def __init__(self, nome: str, cpf, dia: int, mes: int, ano: int, conta: bool = False, id_conta=None):
        if len(cpf) != 11:
            raise ValueError('CPF Inválido')
        else:
            try:
                int(cpf)
            except ValueError:
                raise ValueError('CPF Inválido')
            self.cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}.{cpf[9:11]}'
        self.firstname = nome.upper()
        self.idade = self.calcular_idade(dia, mes, ano)
        self.nascimento = date(day=dia, month=mes, year=ano)
        self.conta = conta
        self.id_conta = id_conta

    def __str__(self):
        return self.firstname

    @staticmethod
    def calcular_idade(dia, mes, ano) -> int:
        born = date(day=dia, month=mes, year=ano)
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))