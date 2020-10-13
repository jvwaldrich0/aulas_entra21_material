from hashlib import sha256
from datetime import date
from random import randint


class Cadastro:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.dados = []
        self.usuario(nome, sobrenome, idade)

    def __repr__(self):
        return self.dados

    def __len__(self):
        return len(self.dados)

    @staticmethod
    def criar_id(nome: str, sobrenome: str, idade: int):
        # -- criar id
        key = randint(1, 100000)  # para criar uma hash mais 'unica'
        primary_id = sha256(str(
            nome +
            sobrenome +
            str(idade) +
            str(key)
        ).encode()
                            ).hexdigest()
        return primary_id

    def usuario(self, nome: str, sobrenome: str, idade: int):
        if self.verificar_idade(idade):
            self.dados += [{'ID': self.criar_id(nome,
                                               sobrenome,
                                               idade),
                           'NOME': nome,
                           'SOBRENOME': sobrenome,
                           'IDADE': idade}]
        else:
            raise ValueError

    def endereco(self, primary_key: str, rua: str, numero: int,
                 complemento: str, bairro: str, estado: str, cidade: str):
        i = self.search(primary_key)
        if primary_key == self.dados[i]:
            self.dados[i]['rua'] = rua
            self.dados[i]['numero'] = numero
            self.dados[i]['complemento'] = complemento
            self.dados[i]['bairro'] = bairro
            self.dados[i]['estado'] = estado
            self.dados[i]['cidade'] = cidade
            print('Endereco adicionado com sucesso')

    def listar_nomes(self):
        for i in range(len(self.dados)):
            if self.dados[i]['NOME'] == None:
                break
            print(f"{self.dados[i]['NOME']}")

    def listar_endereco(self):
        p = []
        for i in range(len(self.dados)):
            for lista in 'ID', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado':
                try:
                    p += [str(self.dados[i][lista])]
                except KeyError:
                    pass
        else:
            return p

    def info_especifico(self, primary_key: str):
        i = self.search(primary_key)
        if primary_key == self.dados[i]:
            return self.dados[i].items()

    @staticmethod
    def verificar_idade(idade) -> bool:
        if idade < 18:
            return False
        else:
            return True

    def key(self, nome):
        for i in range(len(self.dados)):
            if nome == self.dados[i]['NOME']:
                return self.dados[i]['ID']

    def search(self, primary_key: str) -> int:
        for i in range(int(len(self.dados))):
            if primary_key == self.dados[i]['ID']:
                return i


    @staticmethod
    def calculate_age(dia, mes, ano) -> int:
        born = date(day=dia, month=mes, year=ano)
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


