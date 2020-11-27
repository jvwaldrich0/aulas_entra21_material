# DDL - Data Definition Language
# DML - Data Manipulation Language
# DQL - Data Query Language

import sqlite3

conn = sqlite3.connect('poke.db')
cursor = conn.cursor()

lista = [
    ('Bulbasaur', 'planta'),
    ('Charmander', 'fogo'),
    ('Squirtle', 'agua'),
    ('Pikachu', 'elétrico'),
    ('Snorlax', 'normal'),
    ('Mewtwo', 'psiquico'),
    ('Psyduck', 'agua'),
]

try:
    # inserindo dados na tabela através de parâmetros
    cursor.executemany("""
    INSERT INTO pokemons (nome, tipo)
    VALUES (?,?)
    """, lista)
    conn.commit()

except:
    # rollback all database actions since last commit
    conn.rollback()
    raise RuntimeError("Uh oh, an error occurred ...")

print('Dados inseridos com sucesso.')

conn.close()