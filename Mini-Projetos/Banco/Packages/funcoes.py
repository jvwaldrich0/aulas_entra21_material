from os import name, system
from datetime import date


def verificacao(cliente):
    try:
        a = cliente.id_conta.saldo
    except AttributeError:
        raise AttributeError
    else:
        return a

def traco(tamanho: int):
    return '-'*tamanho


def listar(cliente):
    for i in range(len(cliente)):
        print(f'{i} - ' + str(cliente[i]))
    print(traco(24))


def calcular_idade(dia, mes, ano) -> int:
    born = date(day=dia, month=mes, year=ano)
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def clear():
    if name == 'nt':
        # Windows
        return system('cls') or None
    else:
        # Linux / MacOS
        return system('clear') or None


def verify():
    while True:
        quantia = float(input('Digite a quantia\n> '))
        if quantia > 0:
            return quantia
        else:
            print(traco(24) + '\nValor Inválido\n'.upper() + traco(24))


def transferencia(cliente):
    cliente[0]
    indice = []
    controle = True
    for x in range(2):
        print(f'{"De quem" if x == 0 else "Para quem"}')
        for i in range(len(cliente)):
            print(f'{i} - ' + str(cliente[i]))
        indice += [int(input('Digite o índice\n> '))]
        try:
            verificacao(cliente[indice[x]])
        except AttributeError:
            print(traco(24) + f'\n{cliente[indice[x]].firstname} Não possui conta\n'.upper() + traco(24))
            break
    else:
        if controle:
            quantia = verify()
            if quantia > cliente[indice[0]].id_conta.saldo:
                while True:
                    escolha = int(input('SALDO FICARÁ NEGATIVO! '
                                        '\nDIGITE 1 PARA PROSSEGUIR'
                                        '\nDIGITE 2 PARA CANCELAR OPERAÇÃO\n> '))
                    if escolha == 1:
                        cliente[indice[0]].id_conta.saldo -= quantia
                        cliente[indice[1]].id_conta.saldo += quantia
                        break
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
    try:
        verificacao(cliente[indice])
    except AttributeError:
        print(traco(24) + f'\n{cliente[indice].firstname} Não possui conta\n'.upper() + traco(24))
    else:
        cliente[indice].id_conta.saldo += verify()


def view_saldo(cliente):
    cliente[0]
    listar(cliente)
    indice = int(input('Digite o índice\n> '))
    if cliente[indice].conta:
        print(f'{traco(24)}\n{cliente[indice].firstname}: R${cliente[indice].id_conta.saldo:.2f}\n{traco(24)}')
    else:
        print(traco(24) + f'\n{cliente[indice].firstname} não possui saldo\n\nOBS: Crie uma conta'.upper())


def menu():
    return f"""{traco((30))}
Digite a operação desejada
{traco(30)}
1 - Cadastrar Pessoa
2 - Cadastrar Conta
3 - Visualizar Saldo
4 - Fazer uma transferência
5 - Fazer um depósito
6 - Gerenciar Pessoas
7 - Sair
{traco(30)}
> """.upper()


def menu_pessoa(cliente):
    return  f'''{traco((24))}
Nome: {cliente.firstname}
{traco(24)}
CPF: {cliente.cpf}
idade: {cliente.idade}
{traco(24)}
1 - Mudar Nome
2 - Mudar CPF
3 - Mudar data de nascimento
4 - Mudar Saldo
5 - Voltar
{traco(24)}
> '''.upper()


def add_cpf():
    while True:
        cpf1 = input('Digite o CPF(11 caracteres): '.upper())
        if len(cpf1) != 11:
            print(traco(24) + '\nCPF precisa ter 11 caracteres'.upper())
            continue
        else:
            try:
                int(cpf1)
                return cpf1
            except ValueError:
                print(traco(24) + '\nCPF precisa possuir apenas números'.upper())
                continue


def format_cpf(cpf) -> str:
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}.{cpf[9:11]}'


def add_nascimento():
    while True:
        dia1 = int(input('Informe o seu nascimento: \nDia = '))
        mes1 = int(input('Mes = '))
        ano1 = int(input('Ano = '))
        try:
            calcular_idade(dia1, mes1, ano1)
        except ValueError:
            print(traco(24) + '\nData de nascimento inválida\n' + traco(24))
        else:
            return dia1, mes1, ano1
