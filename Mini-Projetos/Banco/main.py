from Packages.banco import Banco, Conta
from Packages.pessoa import Pessoa
from pickle import load, dump
import os

cliente = load(open('Data/data.txt', 'rb'))
path = os.getcwd()

while True:
    try:
        valor = int(input(
            """Digite a operação desejada
1 - Cadastrar Pessoa
2 - Cadastrar Conta
3 - Visualizar Saldo
4 - Fazer um depósito
5 - Sair

> """))
        if valor == 1:
            cliente += [Pessoa(
                nome=input(f'\n\nDigite o nome: '),
                cpf=input('Digite o CPF(11 caracteres): '),
                dia=int(input('Informe o seu nascimento: \nDia = ')),
                mes=int(input('Mes = ')),
                ano=int(input('Ano = ')),
                conta=True
            )]

        elif valor == 2:
            for i in range(len(cliente)):
                print(f'{i} -' + str(cliente[i]))
            indice = int(input('Digite o índice\n> '))
            conta = Conta(
                cliente[indice],
                float(input('Digite o saldo da conta\n> R$'))
            )
            cliente[indice].id_conta = conta
            del indice

        elif valor == 3:
            for i in range(len(cliente)):
                print(f'{i} -' + str(cliente[i]))
            indice = int(input('Digite o índice\n> '))
            if cliente[indice].conta:
                print(f'R${cliente[indice].id_conta.saldo:.2f}')
            del indice
        elif valor == 4:
            indice = []
            for x in range(2):
                print(f'{"De quem" if x == 0 else "Para quem" }')
                for i in range(len(cliente)):
                    print(f'{i} -' + str(cliente[i]))
                indice += [int(input('Digite o índice\n> '))]
            else:
                quantia = float(input('\nDigite a quantia\n > '))
            cliente[indice[0]].id_conta.saldo -= quantia
            cliente[indice[1]].id_conta.saldo += quantia
            del indice
        elif valor == 5:
            print("Agradecemos a sua visita!")
            break
    except ValueError:
        print('Valor Inválido! Reiniciando...')
    else:
        dump(cliente, open('Data/data.txt', 'wb'))
