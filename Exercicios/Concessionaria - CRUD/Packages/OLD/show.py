import sqlite3

bd = sqlite3.connect('veiculos.db')
sql = bd.cursor()

sql.execute('SELECT * FROM veiculos')

print(sql.fetchall())