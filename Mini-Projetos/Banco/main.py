from Packages.banco import Banco, Conta
from Packages.pessoa import Pessoa
from pickle import load, dump
from os.path import join
from os import getcwd as cwd
from shutil import copyfile



def traco(tamanho: int):
    return '-'*tamanho

def indices(indice: int):
    if indice == None:
        pass


try:
    cliente = load(open('Data/data.txt', 'rb'))
    backup = False
    print('Cheguei')
except FileNotFoundError:
    try:
        cliente = load(open('Data/Backup.txt', 'rb'))
        backup = True
    except FileNotFoundError:
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
        print(len(cliente))
        if valor == 1:
            cliente += [Pessoa(
                nome=input(f'{traco(24)}\nDigite o nome: '),
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
            indices(len(cliente))
            for i in range(len(cliente)):
                print(f'{traco(12)}\n{i} -' + str(cliente[i]))
            else:
                print(traco(12))
            indice = int(input('Digite o índice\n> '))
            if cliente[indice].conta:
                print(f'\n{traco(24)}\nR${cliente[indice].id_conta.saldo:.2f}\n{traco(24)}')
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
            for i in range(len(cliente)):
                print(f'{i} -' + str(cliente[i]))
            indice = int(input('Digite o índice\n> '))
            cliente[indice].id_conta.saldo += float(input('\nDigite a quantia\n> '))
            del indice
        elif valor == 6:
            print("Agradecemos a sua visita!")
            break
    except ValueError:
        print('Valor Inválido! Reiniciando...')
    except IndexError:
        print('Indice inexistente')
    else:
        dump(cliente, open('Data/data.txt', 'wb'))


if backup:
    copyfile(join(cwd(), 'Data/Backup.txt'), join(cwd(), 'Data/data.txt'))
