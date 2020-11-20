from pessoas import Pessoa
import sqlite3


p = Pessoa(
    input('Digite algumas informações\nnome: '),
    input('CPF(11 digitos): '),
    int(input('Algumas informações sobre sua data de aniversario\ndia: ')),
    int(input('Mes: ')),
    int(input('Ano: ')),
    input('Voltando a mais algumas coisinhas...\nEndereco: '),
    float(input('Salario: ')),
    input('Profissao: '),
)

bd = sqlite3.connect('pessoas.db')
sql = bd.cursor()

sql.execute('SELECT * FROM pessoas')

print(sql.fetchall())