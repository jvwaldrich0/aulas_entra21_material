from Packages.banco import Banco, Conta
from Packages.pessoa import Pessoa
from Packages.funcoes import verificacao, traco, listar, transferencia, deposito, view_saldo, menu
from pickle import load, dump
from os.path import join
from os import getcwd as cwd
from shutil import copyfile


backup = False
sem_arquivo = False
# Abrir arquivo
try:
    cliente = load(open('Data/data.txt', 'rb'))
    open('Data/Backup.txt', 'rb')
except FileNotFoundError:
    try:
        cliente = load(open('Data/Backup.txt', 'rb'))
        backup = True
    except FileNotFoundError:
        sem_arquivo = True
        cliente = []
while True:
    try:
        # Menu
        valor = int(input(menu()))
        # Cadastrar Pessoa
        if valor == 1:
            cliente += [Pessoa(
                nome=input(f'{traco(24)}\nDigite o nome: '),
                cpf=input('Digite o CPF(11 caracteres): '),
                dia=int(input('Informe o seu nascimento: \nDia = ')),
                mes=int(input('Mes = ')),
                ano=int(input('Ano = ')),
            )]
        # Cadastrar Conta
        elif valor == 2:
            cliente[0]
            listar(cliente)
            indice = int(input('Digite o índice\n> '))
            if cliente[indice].conta:
                print('Conta existente')
            else:
                cliente[indice].id_conta = Conta(
                    cliente[indice],
                    float(input('Digite o saldo da conta\n> R$'))
                )
                cliente[indice].conta = True
            del indice
        # Visualizar Saldo
        elif valor == 3:
            view_saldo(cliente)
        # Transferencia
        elif valor == 4:
            transferencia(cliente)
        # Deposito
        elif valor == 5:
            deposito(cliente)
        # Sair
        elif valor == 6:
            print("Agradecemos a sua visita!")
            break
    except ValueError:
        print('Valor Inválido! Reiniciando...')
    except IndexError:
        print(traco(24), '\nCadastre alguem...\n'.upper() + traco(24))
    else:
        # Salvar arquivo
        dump(cliente, open('Data/data.txt', 'wb'))
# recuperar Backup
if backup:
    copyfile(src=join(cwd(), 'Data/Backup.txt'),
             dst=join(cwd(), 'Data/data.txt'))
# criar arquivo Backup
elif sem_arquivo:
    copyfile(src=join(cwd(), 'Data/data.txt'),
             dst=join(cwd(), 'Data/Backup.txt'))
