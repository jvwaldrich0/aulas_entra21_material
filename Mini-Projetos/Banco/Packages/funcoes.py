from os import name, system


def verificacao(cliente):
    if not cliente.conta:
        return print('Crie uma conta')


def traco(tamanho: int):
    return '-'*tamanho


def listar(cliente):
    for i in range(len(cliente)):
        print(f'{i} - ' + str(cliente[i]))


def clear():
    if name == 'nt': # Windows
        return system('cls') or None
    else: # Linux / MacOS
        return system('clear') or None


def transferencia(cliente):
    cliente[0]
    indice = []
    for x in range(2):
        print(f'{"De quem" if x == 0 else "Para quem"}')
        for i in range(len(cliente)):
            print(f'{i} - ' + str(cliente[i]))
        indice += [int(input('Digite o índice\n> '))]
        verificacao(cliente[indice[x]])
    else:
        quantia = float(input('\nDigite a quantia\n> '))
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


def deposito(cliente):
    cliente[0]
    listar(cliente)
    indice = int(input('Digite o índice\n> '))
    cliente[indice].id_conta.saldo += float(input('\nDigite a quantia\n> '))


def view_saldo(cliente):
    cliente[0]
    listar(cliente)
    print(traco(12))
    indice = int(input('Digite o índice\n> '))
    if cliente[indice].conta:
        print(f'\n{traco(24)}\nR${cliente[indice].id_conta.saldo:.2f}\n{traco(24)}')


def menu():
    return f"""
Digite a operação desejada
{traco(24)}
1 - Cadastrar Pessoa
2 - Cadastrar Conta
3 - Visualizar Saldo
4 - Fazer uma transferência
5 - Fazer um depósito
6 - Sair
{traco(24)}
> """.upper()