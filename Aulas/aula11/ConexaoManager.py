import sqlite3


class Conexao:
    __init__(self):
        pass        

    def conectart(self)
        self.conn = sqlite3.connect('poke.db')
        return self.conn.cursor()

    def desconectar(self)
        self.conn.close()    
