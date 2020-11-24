from datetime import date

from Packages.pessoas import Pessoa
from Packages.veiculos import Veiculos
from Packages.DButils import DatabaseUtils as dbutils
from Packages.Utils import menu, cadastro_veiculos, clear

pessoa = []
veiculo = []
db = dbutils('Data/Concessionaria.db')

while True:
    try:
        clear()
        escolha = int(input(menu()))
        print('-'*20)
    except ValueError:
        print('Inválido')
    else:
        if escolha == 1:
            while True:
                cpf = input('Digite o CPF(11 caracteres): '.upper())
                if len(cpf) != 11:
                    print('\nCPF precisa ter 11 caracteres'.upper())
                    continue
                else:
                    try:
                        int(cpf)
                        break
                    except ValueError:
                        print('\nCPF precisa possuir apenas números'.upper())
                        continue
            while True:
                dia = int(input('Informe o seu nascimento: \nDia = '))
                mes = int(input('Mes = '))
                ano = int(input('Ano = '))
                try:
                    date(ano, mes, dia)
                except ValueError:
                    print('\nData de nascimento inválida\n')
                else:
                    break
            pessoa += [Pessoa(
                nome=input('Nome: '),
                cpf=cpf,
                dia=dia,
                mes=mes,
                ano=ano,
                endereco=input('Endereço: '),
                salario=float(input('Salário: ')),
                profissao=input('Profissao: ')
            )
            ]
            pessoa[len(pessoa) - 1].salvar()
            input('-'*20 + '\nPressione Enter para continuar...')
        elif escolha == 2:
            try:
                nome, marca, modelo, cor, placa, proprietario, num_portas, \
                    km_rodado, qtd_passageiros, ano, valor, motor, combustivel, \
                    meio_locomocao = cadastro_veiculos(pessoa)
                veiculo += [Veiculos(nome, marca, modelo, cor, placa, proprietario,
                                     num_portas, km_rodado, qtd_passageiros, ano,
                                     valor, motor, combustivel, meio_locomocao)]
                veiculo[len(veiculo) - 1].salvar()
            except Exception as e:
                print(e)
                continue
            else:
                print('Veiculo Cadastrado com sucesso')
                input('-' * 20 + '\nPressione Enter para continuar...')
        elif escolha == 3:
            db.listar('pessoas')
            input('-'*20 + '\nPressione Enter para continuar...')
        elif escolha == 4:
            db.listar('veiculos')
            input('-'*20 + '\nPressione Enter para continuar...')
        elif escolha == 5:
            db.listar('pessoas')
            db.rem('pessoas', int(input('Digite o indice:\n> ')))
        elif escolha == 6:
            db.listar('veiculos')
            db.rem('veiculos', int(input('Digite o indice:\n> ')))
        elif escolha == 7:
            break
