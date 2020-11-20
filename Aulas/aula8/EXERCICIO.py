import sqlite3

clientes = sqlite3.connect('clientes.db')

cursor = clientes.cursor()

cursor.execute('''
SELECT alguem FROM algo;
''')

cursor.execute("""
    INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
         VALUES ('Joao', 18, '1075831937', 'jv.waldrich0@protonmail.com', '11-98765-4321', 'Joao', 'SC', '2020-06-08')
""")

print(cursor.fetchone())

cursor.execute('''
CREATE TABLE algo (
    alguem VARCHAR(4)
);
''')

cursor.execute('''
INSERT INTO algo
VALUES ('JACK')''')

clientes.commit()
