import sqlite3
from datetime import date


class Pessoa:
    def __init__(self, nome: str, cpf, dia: int, mes: int, ano: int, endereco: str, salario: float,
                 profissao:str, criar_bd: bool = False):
        self.nome = nome.upper()
        if len(cpf) != 11:
            raise AttributeError('CPF Inválido')
        else:
            try:
                int(cpf)
            except ValueError:
                raise AttributeError('CPF Inválido')
            self.cpf = (f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}.{cpf[9:11]}')
        self.idade = self.calcular_idade(dia, mes, ano)
        # manipular banco de dados
        bd = sqlite3.connect('pessoas.db')
        sql = bd.cursor()
        # caso precise criar um banco de dados
        if criar_bd:
            sql.execute('''
CREATE TABLE pessoas(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cpf TEXT NOT NULL,
    nome TEXT NOT NULL,
    nascimento DATE NOT NULL,
    endereco TEXT NOT NULL,
    salario DECIMAL,
    profissao TEXT);
''')
        lista = [(cpf, nome, f'{ano}/{mes}/{dia}', endereco, salario, profissao)]
        sql.executemany(f'''
INSERT INTO pessoas VALUES(NULL, ?,?,?,?,?,?);''', lista)

        bd.commit()
        bd.close()

    @staticmethod
    def calcular_idade(dia, mes, ano) -> int:
        born = date(day=dia, month=mes, year=ano)
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
