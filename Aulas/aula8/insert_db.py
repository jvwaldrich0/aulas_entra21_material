import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# vamos inserir valores na nossa tabela 
cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
    VALUES ('Regis', 35, '00000000000', 'regis@email.com', '11-98765-4321', 'Sao Paulo', 'SP', '2014-06-08')
""")

# grava no DB
conn.commit()

conn.close()