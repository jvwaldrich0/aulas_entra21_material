"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:
-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair
-----
Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""
class cliente:
    def __init__(self, nome, idade, sexo, telefone):
        self.nome = str(nome).upper()
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone
    def genre(self):
        while True:
            sexo = input('Sexo(M/F): ').upper()
            if sexo == 'M':
                return 'MASCULINO'
            elif sexo == 'F':
                return 'FEMININO'
            else:
                print('Sexo Inválido')
                continue
    def idade(self):
        from datetime import date
        today = date.today()
        print('Por gentileza, Informe sua data de nascimento;')
        while True:
            try:
                dia = int(input('Dia: '))
                mes = int(input('Mês: '))
                ano = int(input('Ano: '))
                nascimento = date(ano,mes,dia)
            except ValueError:
                print('Talvez você tenha digitado algo errado, Informe sua idade novamente por favor')
            else:
                return today.year - nascimento.year - ((today.month, today.day) < (nascimento.month, nascimento.day))

clientes = []
client = cliente(0, 0, 0 ,0)
x = False

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
                idade=cliente.idade(client),
                sexo= cliente.genre(client),
                telefone=input('Telefone: ')
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