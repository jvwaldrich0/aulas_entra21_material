from ClasseC import cliente

clientes = []
x = False
client

while True:
    try:
        escolha = input('''-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair
-----
> '''.upper()).upper()
        if escolha == 'A':
            clientes += [cliente(
                nome=input('Nome: '),
                idade=cliente.idade(),
                sexo= cliente.genre(sexo=input('Digite seu sexo: '.upper())),
                telefone=int(input('Telefone: '))
            )]
        elif escolha == 'B':
            print('Nomes cadastrados')
            for i in range(len(clientes)):
                print(f'{i} - {clientes[i].nome}', sep='\n')
        elif escolha == 'C':
            buscador = input('Nome: ').upper()
            for i in range(len(clientes)):
                if buscador == str(clientes[i].nome).upper():
                    print(f'''-----
NOME = {clientes[i].nome}
IDADE = {clientes[i].idade}
SEXO = {clientes[i].sexo}
TELEFONE = {clientes[i].telefone}''')
                    x = True
                    break
                else:
                    x = False
            else:
                if x == False:
                    print('\nNOME NÃO ENCONTRADO!\n')
        elif escolha == 'D':
            buscador = input('Nome: ').upper()
            for i in range(len(clientes)):
                if buscador == str(clientes[i].nome).upper():
                    clientes.pop(i)
        elif escolha == 'S':
            print('Saindo...')
            break
    except ValueError:
        print('Digito errado!')
        continue