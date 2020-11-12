from random import randint
from datetime import date


class Banco():
    def __init__(self):
        self.agencia = randint(1000, 9999)
        self.conta = f'{randint(1000000, 9999999)}-{randint(0, 9)}'
        self.codseg = randint(100, 999)


class Conta():
    def __init__(self, banco: Banco, pessoa, saldo = 0.00):
        self.id = pessoa.cpf
        self.banco = banco
        self.pessoa = pessoa
        self.saldo = saldo


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


if __name__ == "__main__":
    cliente = []
    while True:
        try:
            valor = int(input(
                """Digite a operação desejada
1 - Cadastrar Pessoa
2 - Cadastrar Conta
3 - Visualizar Saldo
4 - Fazer um depósito
5 - Sair

> """))
            if valor == 1:
                cliente += [Pessoa(
                    nome=input(f'\n\nDigite o nome: '),
                    cpf=input('Digite o CPF(11 caracteres): '),
                    dia=int(input('Informe o seu nascimento: \nDia = ')),
                    mes=int(input('Mes = ')),
                    ano=int(input('Ano = ')),
                    conta=True
                )]

            elif valor == 2:
                for i in range(len(cliente)):
                    print(f'{i} -' + str(cliente[i]))
                indice = int(input('Digite o índice\n> '))
                conta = Conta(
                    Banco(),
                    cliente[indice],
                    float(input('Digite o saldo da conta\n> R$'))
                )
                cliente[indice].id_conta = conta
                del indice

            elif valor == 3:
                for i in range(len(cliente)):
                    print(f'{i} -' + str(cliente[i]))
                indice = int(input('Digite o índice\n> '))
                if cliente[indice].conta:
                    print(f'R${cliente[indice].id_conta.saldo:.2f}')
                del indice

            elif valor == 4:
                indice = []
                for x in range(2):
                    print(f'{"De quem" if x == 0 else "Para quem" }')
                    for i in range(len(cliente)):
                        print(f'{i} -' + str(cliente[i]))
                    indice += [int(input('Digite o índice\n> '))]
                else:
                    quantia = float(input('\nDigite a quantia\n > '))
                cliente[indice[0]].id_conta.saldo -= quantia
                cliente[indice[1]].id_conta.saldo += quantia
                del indice
            elif valor == 5:
                print("Agradecemos a sua visita!")
                break

        except ValueError:
            pass

        else:
            pass

