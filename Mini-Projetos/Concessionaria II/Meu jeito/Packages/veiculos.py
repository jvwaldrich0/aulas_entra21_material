import sqlite3


class Veiculos:
    '''
    Classe Veiculos tem como objetivo cadastrar veiculos de acordo com os atributos mencionados
no __init__, todos os dados de cadastro entra no banco de dados
    '''

    def __init__(self, nome: str, marca: str, modelo: str, cor: str, placa: str,
                 proprietario: int, ano: int, valor: float, motor: float, combustivel: str,
                 meio_locomocao: str, num_portas: int = 4, km_rodado: int = 0,
                 qtd_passageiros: int = 5):
        # Adicionando nos atributos da classe
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.cor = cor
        self.nome = nome
        self.placa = placa
        self.proprietario = proprietario
        self.num_portas = num_portas
        self.km_rodado = km_rodado
        self.qtd_passageiros = qtd_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.meio_locomocao = meio_locomocao
        # Chamando o banco de dados
        self.bd = sqlite3.connect('Data/Concessionaria.db')
        self.sql = self.bd.cursor()
        try:
            # Criar tabela caso não exista
            self.sql.execute("""
CREATE TABLE veiculos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome Varchar(50),
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        cor TEXT,
        placa VARCHAR(7),
        proprietario INTEGER,
        num_portas INT,
        km_rodado INT,
        qtd_passageiros INT,
        ano INTEGER,
        valor INTEGER,
        motor INT,
        combustivel VARCHAR(20),
        meio_locomocao VARCHAR(30),
        
        FOREIGN KEY (proprietario) REFERENCES pessoas(id));
""")
        except sqlite3.OperationalError:
            # Caso exista a tabela selecione a tabela
            self.sql.execute('SELECT * FROM veiculos')

    def salvar(self):
        try:
            # Inserindo no banco de dados
            self.sql.executemany('''INSERT INTO veiculos(
                    nome, marca, modelo, cor, placa,
                    proprietario, num_portas, km_rodado,qtd_passageiros, ano,
                    valor, motor, combustivel, meio_locomocao)
                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                                 [(self.nome, self.marca, self.modelo, self.cor, self.placa,
                                   self.proprietario, self.num_portas, self.km_rodado, self.qtd_passageiros, self.ano,
                                   self.valor, self.motor, self.combustivel, self.meio_locomocao)])
        except:
            # Se der erro ele desfaz
            print('Deu problema')
            self.bd.rollback()
        else:
            #  Caso não de erro grava os dados
            self.bd.commit()
            print('Veiculo cadastrado com sucesso')

    def dados_veiculos(self, id: int = 0) -> list:
        self.sql.execute(f'SELECT * FROM veiculos WHERE id = {id} ')
        return self.sql.fetchall()
