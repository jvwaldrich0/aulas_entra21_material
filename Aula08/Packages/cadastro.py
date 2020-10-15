import pandas as pd
from hashlib import sha3_512 as sha512
from random import randint as r_int
from math import pow
from datetime import date

class Cadastro:
    # Comportamento
    def __init__(self, arquivo, cond: bool):
        if not cond:
            dados = [self.__hash__(),'Joao', 'Waldrich', 18,'SC', 'Gaspar', 'BairroJoao',
                     'RuaJoao', 21, 'uma residencia']
            df = pd.DataFrame(data=[dados],columns=['ID', 'Nome', 'Sobrenome', 'Idade',
                                                  'Estado', 'Cidade', 'Bairro',
                                                  'Rua', 'Numero', 'Complemento'])
            df.to_csv('Planilhas/'+arquivo+'.csv')
        self.data = pd.read_csv('Planilhas/' + arquivo + '.csv', index_col=0)
        self.arquivo = arquivo
        pd.set_option('max_colwidth', 800)
    def __repr__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def __hash__(self):
        return str(sha512(str(
            self.gen() + self.gen() + self.gen()).encode()).hexdigest())

    # Funções
    # --- Manipular cadastro
    def add_user(self, nome, sobrenome, idade: int, ):
        if idade >= 18:
            self.data.loc[len(self.data)] = [self.__hash__(), nome, sobrenome, idade,
                                             '', '', '', '', '', '']
            self.data.to_csv('Planilhas/'+self.arquivo+'.csv')
        else:
            return AttributeError

    def add_home(self, row, Estado, Cidade, Bairro, Rua, Numero: int, Complemento):
        lista = [Estado, Cidade, Bairro, Rua, Numero, Complemento]
        lista2 = ['Estado', 'Cidade', 'Bairro', 'Rua', 'Numero', 'Complemento']
        for i in range(len(lista)):
            self.data.at[row, lista2[i]] = lista[i]
        else:
            print('\nArmazenamento Concluído...\n')
            self.data.to_csv('Planilhas/'+self.arquivo+'.csv')

    def remove(self, row):
        self.data = self.data.drop(row)
        self.data.to_csv('Planilhas/' + self.arquivo + '.csv')

    def edit(self, row, colum, input):
        self.data.at[row, colum] = input
        self.data.to_csv('Planilhas/' + self.arquivo + '.csv')

    # --- Utilitarios de cadastro
    @staticmethod
    def calcular_idade(dia, mes, ano) -> int:
        born = date(day=dia, month=mes, year=ano)
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    # --- Outros
    def listar(self, col_nome):
        return self.data[col_nome]

    def info(self, row):
        return self.data.loc[row]

    @staticmethod
    def print_endereco():
        return ['Nome', 'Sobrenome', 'Idade', 'Estado', 'Cidade', 'Bairro', 'Rua', 'Numero', 'Complemento']

    @staticmethod
    def gen():
        return str(r_int(1, pow(64, 10)))