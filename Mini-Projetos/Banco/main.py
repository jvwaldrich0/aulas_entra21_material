from Packages.banco import Banco, Conta
from Packages.pessoa import Pessoa
from Packages.funcoes import verificacao, traco, listar
from pickle import load, dump
from os.path import join
from os import getcwd as cwd
from shutil import copyfile


backup = False
sem_arquivo = False
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
        valor = int(input(
            f"""
Digite a operação desejada
{traco(24)}
1 - Cadastrar Pessoa
2 - Cadastrar Conta
3 - Visualizar Saldo
4 - Fazer uma transferência
5 - Fazer um depósito
6 - Sair
{traco(24)}
> """.upper()))
        if valor == 1:
            cliente += [Pessoa(
                nome=input(f'{traco(24)}\nDigite o nome: '),
                cpf=input('Digite o CPF(11 caracteres): '),
                dia=int(input('Informe o seu nascimento: \nDia = ')),
                mes=int(input('Mes = ')),
                ano=int(input('Ano = ')),
            )]


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

        elif valor == 3:
            cliente[0]
            listar(cliente)
            print(traco(12))
            indice = int(input('Digite o índice\n> '))
            if cliente[indice].conta:
                print(f'\n{traco(24)}\nR${cliente[indice].id_conta.saldo:.2f}\n{traco(24)}')
            del indice

        elif valor == 4:
            cliente[0]
            indice = []
            for x in range(2):
                print(f'{"De quem" if x == 0 else "Para quem" }')
                for i in range(len(cliente)):
                    print(f'{i} - ' + str(cliente[i]))
                indice += [int(input('Digite o índice\n> '))]
                print(verificacao(cliente[indice[x]]))
            else:
                quantia = float(input('\nDigite a quantia\n > '))
                if quantia > cliente[indice[0]].id_conta.saldo:
                    escolha = 0
                    while escolha != 1 or 2:
                        escolha = int(input('SALDO FICARÁ NEGATIVO! '
                                            'DIGITE 1 PARA PROSSEGUIR'
                                            'DIGITE 2 PARA CANCELAR OPERAÇÃO'))
                        if escolha == 1:
                            cliente[indice[0]].id_conta.saldo -= quantia
                            cliente[indice[1]].id_conta.saldo += quantia
                        elif escolha == 2:
                            break
                        else:
                            continue
                else:
                    cliente[indice[0]].id_conta.saldo -= quantia
                    cliente[indice[1]].id_conta.saldo += quantia
            del indice
        elif valor == 5:
            cliente[0]
            listar(cliente)
            indice = int(input('Digite o índice\n> '))
            cliente[indice].id_conta.saldo += float(input('\nDigite a quantia\n> '))
            del indice

        elif valor == 6:
            print("Agradecemos a sua visita!")
            break
    except ValueError:
        print('Valor Inválido! Reiniciando...')
    except IndexError:
        print(traco(24),'\nCadastre alguem...\n'.upper() + traco(24))
    else:
        dump(cliente, open('Data/data.txt', 'wb'))

if backup:
    copyfile(src=join(cwd(), 'Data/Backup.txt'), dst=join(cwd(), 'Data/data.txt'))
elif sem_arquivo:
    copyfile(src=join(cwd(), 'Data/data.txt'), dst=join(cwd(), 'Data/Backup.txt'))
