import sqlite3
from datetime import date


class Pessoa:
    def __init__(self, nome: str, cpf, dia: int, mes: int, ano: int,
                 endereco: str, salario: float,profissao:str):
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.nome = nome.upper()
        if len(cpf) != 11:
            raise AttributeError('CPF Inválido')
        else:
            try:
                int(cpf)
            except ValueError:
                raise AttributeError('CPF Inválido')
            self.cpf = (f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}')
        self.idade = self.calcular_idade(dia, mes, ano)
        # manipular banco de dados
        self.bd = sqlite3.connect('Data/Concessionaria.db')
        self.sql = self.bd.cursor()
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        try:
            # Criar tabela caso não exista
            self.sql.execute('''
    CREATE TABLE pessoas(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cpf TEXT NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        endereco TEXT NOT NULL,
        salario DECIMAL,
        profissao TEXT);
    ''')
        except sqlite3.OperationalError:
            # Caso exista a tabela selecione a tabela
            self.sql.execute('SELECT * FROM pessoas')

    def salvar(self):
        try:
            # Inserindo no banco de dados
            self.sql.executemany('INSERT INTO pessoas VALUES(NULL, ?,?,?,?,?,?);',
                    [(self.cpf, self.nome, f'{self.ano}/{self.mes}/{self.dia}',
                    self.endereco, self.salario, self.profissao)])
        except:
            # Se der erro ele desfaz
            print('Deu problema')
            self.bd.rollback()
        else:
            #  Caso não de erro grava os dados
            self.bd.commit()
            print('Pessoa cadastrada com sucesso')

    @staticmethod
    def calcular_idade(dia, mes, ano) -> int:
        born = date(day=dia, month=mes, year=ano)
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
