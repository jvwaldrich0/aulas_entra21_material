from datetime import date


class Pessoa:
    def __init__(self, nome: str, cpf, dia: int, mes: int, ano: int, motorista: bool = False, habilitacao: bool = False):
        self.firstname = nome.upper().split(' ')[0]
        if len(cpf) != 11:
            raise AttributeError('CPF Inválido')
        else:
            try:
                int(cpf)
            except ValueError:
                raise AttributeError('CPF Inválido')
            self.cpf = (f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}.{cpf[9:11]}')
        self.idade = self.calcular_idade(dia, mes, ano)
        if motorista and habilitacao:
            self.habilitacao = True
            self.motorista = True
        else:
            self.motorista = False
            self.habilitacao = habilitacao

    def __str__(self):
        if self.motorista:
            return f'O/A motorista é {self.firstname}, portador(a) do cpf {self.cpf} e possui {self.idade} anos de idade'
        else:
            return f'{self.firstname} é passageiro(a), portador(a) do cpf {self.cpf} e possui {self.idade} anos de idade'

    @staticmethod
    def calcular_idade(dia, mes, ano) -> int:
        born = date(day=dia, month=mes, year=ano)
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
