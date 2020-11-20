from datetime import date

from Packages.pessoas import Pessoa
from Packages.veiculos import Veiculos
from Packages.DButils import Database_Utils as dbutils
from Packages.utils import menu, cadastro_veiculos

pessoa = []
veiculo = []
db = dbutils('Data/Concessionaria.db')

while True:
    try:
        escolha = int(input(menu()))
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
                nome = input('Nome: '),
                cpf = cpf,
                dia = dia,
                mes = mes,
                ano = ano,
                endereco = input('Endereço: '),
                salario = float(input('Salário: ')),
                profissao = input('Profissao: ')
            )]
            pessoa[len(pessoa)-1].salvar()
            print('Pessoa cadastrada com sucesso')
        elif escolha == 2:
            try:
                nome, marca, modelo, cor, placa, proprietario, num_portas,\
                km_rodado, qtd_passageiros, ano, valor, motor, combustivel,\
                meio_locomocao = cadastro_veiculos(pessoa)
            except:
                print('\nCadastre Alguem!\n')
                continue

            veiculo += [Veiculos(nome, marca, modelo, cor, placa, proprietario,
                                 num_portas, km_rodado, qtd_passageiros, ano,
                                 valor,motor, combustivel, meio_locomocao)]

            veiculo[len(veiculo)-1].salvar()
            print('Veiculo cadastrado com sucesso')
        elif escolha == 3:
            db.listar('pessoas')
        elif escolha == 4:
            db.listar('veiculos')
        elif escolha == 5:
            break
