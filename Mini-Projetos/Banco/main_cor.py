from Packages.banco import Banco, Conta
from Packages.pessoa import Pessoa
from Packages.funcoes import calcular_idade, verificacao, traco, listar, transferencia, deposito, view_saldo, menu
from Packages.cor import cor
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
        valor = int(input(cor.END + cor.BOLD + menu()))
        # Cadastrar Pessoa
        if valor == 1:
            print(cor.BLUE)
            nome1 = input(f'{traco(24)}\nDigite o nome: '.upper())
            while True:
                cpf1 = input('Digite o CPF(11 caracteres): '.upper())
                if len(cpf1) != 11:
                    print(traco(24)+'\nCPF precisa ter 11 caracteres'.upper())
                    continue
                else:
                    try:
                        int(cpf1)
                        break
                    except ValueError:
                        print(traco(24)+'\nCPF precisa possuir apenas números'.upper())
                        continue
            while True:
                dia1 = int(input('Informe o seu nascimento: \nDia = '))
                mes1 = int(input('Mes = '))
                ano1 = int(input('Ano = '))
                try:
                    calcular_idade(dia1, mes1, ano1)
                except ValueError:
                    print(traco(24)+'\nData de nascimento inválida\n'+traco(24))
                else:
                    break

            cliente += [Pessoa(
                nome=nome1,
                cpf=cpf1,
                dia=dia1,
                mes=mes1,
                ano=ano1,
            )]
        # Cadastrar Conta
        elif valor == 2:
            print(cor.YELLOW + traco(24))
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
            print(cor.CYAN + traco(24))
            view_saldo(cliente)
        # Transferencia
        elif valor == 4:
            print(cor.DARKCYAN + traco(24))
            transferencia(cliente)
        # Deposito
        elif valor == 5:
            print(cor.RED + traco(24))
            deposito(cliente)
        # Sair
        elif valor == 6:
            print(cor.PURPLE + traco(24))
            print("Agradecemos a sua visita!".upper())
            break
        else:
            print(traco(20) + '\nOpção inválida\n'.upper() + traco(20))
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
