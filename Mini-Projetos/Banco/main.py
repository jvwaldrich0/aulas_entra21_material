# Standart Libraries Import
from pickle import load, dump
from os.path import join
from os import getcwd as cwd
from shutil import copyfile
from datetime import date

# Importando funções de pasta Packages
from Packages.banco import Banco, Conta
from Packages.pessoa import Pessoa
from Packages.funcoes import format_cpf, add_nascimento, add_cpf, menu_pessoa, calcular_idade, verificacao, traco, listar, transferencia, deposito, view_saldo, menu


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
        print(traco(24))
        # Cadastrar Pessoa
        if valor == 1:
            nome1 = input(f'Digite o nome: '.upper())
            cpf1 = add_cpf()
            dia1, mes1, ano1 = add_nascimento()
            cliente += [Pessoa(
                nome=nome1,
                cpf=cpf1,
                dia=dia1,
                mes=mes1,
                ano=ano1,
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
        # Gerenciar Pessoas
        elif valor == 6:
            listar(cliente)
            indice = int(input('Digite o índice\n> '))
            escolha = int(input(menu_pessoa(cliente[indice])))
            # Mudar Nome
            if escolha == 1:
                cliente[indice].firstname = input(f'{traco(24)}\nDigite o novo nome\n> ').upper()
            # Mudar CPF
            elif escolha == 2:
                cliente[indice].cpf = format_cpf(add_cpf())
            # Mudar data de nascimento
            elif escolha == 3:
                dia1, mes1, ano1 = add_nascimento()
                cliente[indice].nascimento = date(day=dia1,
                                                  month=mes1,
                                                  year=ano1)
                cliente[indice].idade = calcular_idade(dia1,
                                                       mes1,
                                                       ano1)
            # Mudar Saldo
            elif escolha == 4:
                try:
                    cliente[indice].id_conta.saldo = float(input(
                        f'R${cliente[indice].id_conta.saldo:.2f}\nDIGITE O NOVO SALDO\n> '))
                except AttributeError:
                    print(traco(24) + f'\n{cliente[indice].firstname} não possui saldo\n\nOBS: Crie uma conta'.upper())
            # Volta
            elif escolha == 5:
                continue
        # Sair
        elif valor == 7:
            print(traco(24))
            print("Agradecemos a sua visita!".upper())
            break
        else:
            print(traco(20) + '\nOpção inválida\n'.upper() + traco(20))
    except ValueError:
        print('Valor Inválido! Reiniciando...')
    except IndexError:
        print(traco(24), '\nCadastre alguém...\n'.upper() + traco(24))
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
