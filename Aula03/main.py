from Packages.cadastro import Cadastro
from Packages import menu

print('Irei pedir um cadastro para começar')
try:
    cadastro = Cadastro(
        input('Digite seu primeiro nome: ').upper(),
        input('Digite seu sobrenome: ').upper(),
        Cadastro.calculate_age(
            int(input('Dia de nascimento: ')),
            int(input('Mes de nascimento: ')),
            int(input('Ano de nascimento: ')))
    )

    dono = input('\nDigite o nome de uma/um empresa/usuario: ')

    print('Bem-vindo ao software de cadastro versão beta')

    while True:
        escolha = int(input(f'''{menu.cabecalho(6, dono)}
1 - Cadastrar usuário
2 - Cadastrar rua
3 - Listar pessoas
4 - Listar endereços
5 - Informação específica
6 - Sair

>'''))
        if escolha == 1:
            cadastro.usuario(
                input('Digite seu primeiro nome: ').upper(),
                input('Digite seu sobrenome: ').upper(),
                Cadastro.calculate_age(
                    int(input('Dia de nascimento: ')),
                    int(input('Mes de nascimento: ')),
                    int(input('Ano de nascimento: ')))
            )
        elif escolha == 2:
            print(cadastro.listar_nomes())
            cadastro.endereco(
                    cadastro.key(input('Nome: ').upper()),
                    input('Rua: '),
                    int(input('Número: ')),
                    input('Complemento: '),
                    input('Bairro: '),
                    input('Estado: '),
                    input('Cidade: ')
            )
        elif escolha == 3:
            print(cadastro.listar_nomes(), sep='\n')
        elif escolha == 4:
            print(cadastro.listar_endereco())

except ValueError:
    c = open('log.txt', 'x')
    c.write(f'{}')
