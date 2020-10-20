from Packages.cadastro import Cadastro


# - Função de aviso
def aviso():
    print('\nOps, parece que você digitou algo errado.\nVamos tentar de novo\n')


# - Nota de autor e de versão
print('\nSoftware de cadastro feito por João Vitor Waldrich versão Beta 1.0\n')

# - Instanciando a função Cadastro
empresa_cadastro = input('Digite o arquivo de cadastro .csv que você deseja manipular\n> ').upper()
if empresa_cadastro == '':
    empresa_cadastro = 'ENTRA21'
try:
    df = Cadastro(empresa_cadastro, True)
except FileNotFoundError:
    df = Cadastro(empresa_cadastro, False)

# - Menu Personalizável
menu = '-' * 15 + ' Menu ' + empresa_cadastro + ' ' + '-' * 15

# - Variavel de controle
controle = False

while True:
    try:
        # - Menu de escolha das opções
        escolha = int(input(f'''
{menu}
1 - Cadastrar usuário
2 - Adicionar endereço a um usuário
3 - Editar cadastro
4 - Remover cadastros
5 - Listar nomes cadastrado
6 - Ver todas as informações de um usuário
7 - Sair
{menu}\n> '''))
    except ValueError:  # Caso o usuário digite algum caracter inválido
        aviso()
        continue
    else:
        if escolha == 1:
            while True:
                try:
                    df.add_user(
                        input('Nome: '),
                        input('Sobrenome: '),
                        df.calcular_idade(
                            int(input('Agora algumas informações sobre seu aniversário\nDia:')),
                            int(input('Mês: ')),
                            int(input('Ano: '))
                        )
                    )
                except ValueError:
                    aviso()
                    continue
                except AttributeError:
                    print('\nMenor de 18 anos\n')
                    continue
                else:
                    x = int(input('Digite 1 para acrescentar um endereço também!\n>'))
                    # Colocando usuário direto para a segunda opção caso ele concorde em add endereço também
                    if x == 1:
                        controle = True
                        escolha = 2
                        row = len(df) - 1
                    else:
                        controle = False
                    break
        if escolha == 2:
            while True:
                try:
                    if not controle:
                        print(df.listar('Nome'))
                        row = int(input('Quem você deseja editar?(Digite o número ao lado)\n>'))
                    df.add_home(
                        row,
                        input('Estado: '),
                        input('Cidade: '),
                        input('Bairro: '),
                        input('Rua: '),
                        int(input('Número: ')),
                        input('Complemento: ')
                    )
                except ValueError:
                    aviso()
                    continue
                else:
                    break
        elif escolha == 3:
            while True:
                try:
                    print(df.listar('Nome'), '\n')
                    x = int(input('\nDigite o número correspondente ao nome: '))
                    print(*df.print_endereco(), sep='\n')
                    y = input('Digite um destes itens que deseja mudar\n> ')
                    if y == 'ID':
                        print('\nCampo Indisponível\n')
                        continue
                    campo = input(f'O que você deseja colocar neste campo: ')
                    df.edit(x, y, campo)
                except ValueError:
                    aviso()
                    continue
                else:
                    break
        elif escolha == 4:
            while True:
                try:
                    print(df.listar('Nome'), '\n')
                    df.remove(
                        int(input('\nDigite o número correspondente ao nome: '))
                    )
                except ValueError:
                    aviso()
                    continue
                else:
                    break
        elif escolha == 5:
            print(df.listar('Nome'), '\n')
        elif escolha == 6:
            while True:
                try:
                    print(df.listar('Nome'), '\n')
                    print(df.info(
                        int(input('\nDigite o número correspondente ao nome: '))
                    ))
                except ValueError:
                    aviso()
                    continue
                else:
                    break
        elif escolha == 7:
            print('Saindo...')
            break
        elif escolha == 1:
            pass
        else:
            print('\nNúmero Inválido!\n')
            continue
        del escolha
