import sqlite3


conn = sqlite3.connect('veiculos.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE veiculos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome Varchar(50),
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        cor TEXT,
        placa VARCHAR(7),
        proprietario VARCHAR(50),
        num_portas INT,
        km_rodado INT,
        qtd_passageiros INT,
        ano INTEGER,
        valor INTEGER,
        motor INT,
        combustivel VARCHAR(20),
        meio_locomocao VARCHAR(30)

);
""")
#
# print('Tabela criada com sucesso.')
#
# conn.commit()
# conn.close()


class Veiculo:
    def __init__(self, nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado,
                 qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao):
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
        lista = [(nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado,
                  qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao)]
        print(lista[0])
        bd = sqlite3.connect('veiculos.db')
        sql = bd.cursor()

        sql.executemany('''
                INSERT INTO veiculos(nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado,qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                        lista)
        bd.commit()
        bd.close()
        print('Cadastrado com sucesso')

    def salvar_veiculo(self):
        bd = sqlite3.connect('veiculos.db')
        sql = bd.cursor()

        sql.executemany('''
        INSERT INTO veiculos(nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado,qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',
                        self.lista)
        bd.commit()
        bd.close()


def cadastro_veiculos():
    print("\n\t__________CADASTRO DE VEÍCULOS__________\n")
    nome = input('Nome do Carro: '),
    marca = input("Marca: "),
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    placa = input("Placa: ")
    proprietario = input("Nome do proprietário: ")
    num_portas = int(input("Número de portas: "))
    km_rodado = int(input("Km rodado: "))
    qtd_passageiros = int(input("Quantidade máxima de passageiros: "))
    ano = int(input("Ano: "))
    valor = int(input("Valor: R$ "))
    motor = float(input("Motor: "))
    combustivel = input("Tipo de combustível: ")
    meio_locomocao = input("Meio de locomoção: ")

    veiculos = [nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, qtd_passageiros, ano, valor,
                motor, combustivel, meio_locomocao]
    return nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, \
           qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao


nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao = cadastro_veiculos()
print(nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, qtd_passageiros, ano, valor, motor,
      combustivel, meio_locomocao)
print(nome[2:])
veiculo = Veiculo(str(nome).replace(',''('')',''), str(marca).replace(',',''), modelo, cor, placa, proprietario, num_portas, km_rodado, qtd_passageiros, ano, valor,
                  motor, combustivel, meio_locomocao)
