from random import randint


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