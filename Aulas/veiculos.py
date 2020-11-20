import sqlite3

veiculos = sqlite3.connect('veiculos.db')

terminal = veiculos.cursor()

terminal.execute('''
CREATE TABLE corola (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cor TEXT NOT NULL,
    dono TEXT,
    ano INTEGER NOT NULL
);
''')

terminal.execute('''
INSERT INTO corola (cor, dono, ano)
VALUES (verl)
''')

veiculos.commit()

veiculos.close()
