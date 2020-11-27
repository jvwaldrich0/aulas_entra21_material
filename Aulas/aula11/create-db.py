#sqlite3 já faz parte do python :D
import sqlite3

# isso cria o banco, caso não exista!
conn = sqlite3.connect('poke.db')


# para fazermos nossas operações, sempre precisaremos de um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.executescript("""
CREATE TABLE treinadores(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cidade TEXT
);
CREATE TABLE pokemons (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tipo TEXT NOT NULL
);
CREATE TABLE pokemons_treinador (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_treinador INTEGER NOT NULL,
        id_pokemon INTEGER NOT NULL,
        data_capturado DATE,
        
        FOREIGN KEY (id_treinador) references treinadores(id),
        FOREIGN KEY (id_pokemon) references pokemons(id)
);
""")

print('Tabela criada com sucesso.')
# isso fecha a conexão
conn.close()