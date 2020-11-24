from sqlite3 import connect
from Packages.DButils import DatabaseUtils as dbutils


def menu():
    return '''
------- Menu -------

1 - Cadastrar Pessoa
2 - Cadastrar Veiculo
3 - Listar Pessoa
4 - Listar Veiculos
5 - Sair

> '''


def cadastro_veiculos(pessoas):
    print("\n\t__________CADASTRO DE VEÍCULOS__________\n")
    nome = input('Nome do Carro: ')
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    placa = input("Placa: ")
    print('Escolha um proprietario: ')
    # Tentar listar os usuarios
    db = dbutils('Data/Concessionaria.db')
    db.listar('pessoas')
    proprietario = int(input('\n> '))
    num_portas = int(input("Número de portas: "))
    km_rodado = int(input("Km rodado: "))
    qtd_passageiros = int(input("Quantidade máxima de passageiros: "))
    ano = int(input("Ano: "))
    valor = int(input("Valor: R$ "))
    motor = float(input("Motor: "))
    combustivel = input("Tipo de combustível: ")
    meio_locomocao = input("Meio de locomoção: ")

    # Tratamento
    # nome = nome[1:].replace("',)")
    # marca = marca[1:].replace("',)")

    return nome, marca, modelo, cor, placa, proprietario, \
            num_portas, km_rodado, qtd_passageiros, ano, valor, \
            motor, combustivel, meio_locomocao
