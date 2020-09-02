'''
Exercício 01
Crie um programa que cadastre 5 clientes.
Cada cliente possui: Nome, sexo, Telefone
(Guarde estes dados em listas separadas).
Depois mostre os dados cadastrados no seguinte formato:
***********************************
Relatório de clientes cadastrados 
***********************************
Nome: 
Sexo:
Telefone:
***********************************
Exercício 02

O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

Exemplo:
id: 1
Nome: Dudu

id: 2
Nome: Marta

ATENÇÃO!!!!
O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.

Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
(cadastre no minimo 4 clientes)
3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.
3.2) Depois mostre os dados dos 5 clientes.
3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.
3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
- Para menores de 17 anos: Entrada Proibida
- Para maiores de 17 anos: Entrada Liberada
- Para o sexo Feminino: 50% de desconto
- Para o sexo Masculino: 5% de desconto

Minha analise:
- Atributos = id(chave primaria), nome, idade, sexo, telefone
- Objetivo: Criar um software de cadastro, cada user possui uma chave primária
'''
################################################################################
#                                 Classes                                      #
################################################################################
# --- Classe para adicionar algumas cores :) --- #
##################################################
class cor:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
##################################################
# --- Classe cliente (Don't repeat yourself) --- #
##################################################
class cliente:
    def __init__(self, id, nome, idade, sexo, telefone): # ---- Construtor
        self.id = id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone

    def sex(self, sexo):
        if str(sexo).upper() == 'F':
            return 'FEMININO'
        if str(sexo).upper() == 'M':
            return 'MASCULINO'
        else:
            return 'INDEFINIDO'

    def filtro(self, idade, item):
        if idade >= 18:
            if cliente.sex(self=usuario[item], sexo=usuario[i].sexo) == 'FEMININO':
                return 'Entrada Liberada - MULHERES POSSUEM 50% DE DESCONTO'
            elif cliente.sex(self=usuario[item], sexo=usuario[i].sexo) == 'MASCULINO':
                return 'Entrada Liberada - HOMENS POSSUEM 5% DE DESCONTO'
            else:
                return 'Entrada Liberada - SEXO INDEFINIDO NÂO POSSUI DESCONTO'
        else:
            return 'Entrada Proibida'

    def difference(self, item):
        if cliente.sex(self=usuario[item], sexo=usuario[i].sexo) == 'FEMININO':
            return cor.PURPLE
        elif cliente.sex(self=usuario[item], sexo=usuario[i].sexo) == 'MASCULINO':
            return cor.BLUE
        else:
            return cor.GREEN

    def relatorio(self, item, color):
        print(cor.BOLD + color + f'''
***********************************************************
ID: {usuario[item].id}
***********************************************************
Nome:       {usuario[item].nome}
Idade:      {usuario[item].idade}
Sexo:       {cliente.sex(self=usuario[item], sexo=usuario[i].sexo)}
Telefone:   {usuario[item].telefone}
***********************************************************
{cliente.filtro(usuario[item], usuario[item].idade, item)}
***********************************************************
''' + cor.END)
######################################################################################
#      AVISO!     #
###################
print(cor.BOLD+cor.CYAN+'\n\tO código ficou um pouco extenso, eu ia dividir ele em alguns arquivos e apenas importar, mas para facilitar a correção eu coloquei tudo em um único arquivo.\n'.upper()+cor.END)
# --- Instância da classe em uma lista --- #
usuario = []

################################################################################
#                                  Main                                        #
################################################################################
while True:
    try:
        escolha = int(input(cor.BOLD + '''
1 - Cadastrar usuário
2 - Relatório de clientes cadastrados (Exercício 1)
3 - Mostrar Informaçôes de um usuário (Exercício 2 e 3)

(Pressione qualquer tecla para sair)
> '''.upper()))
    except ValueError:
        print('Saindo...')
        break
    else:
        # --- if de escolhas --- #
        if escolha == 1:
            # --- Loop para construçâo dos dados --- #
            while True:
                try:
                    usuario += [cliente(
                        id=len(usuario),
                        nome=input(cor.BOLD + 'NOME: ').upper(),
                        idade=int(input('IDADE: ')),
                        sexo=str(input(f'SEXO ({cor.BLUE + "M" + cor.END + "/" + cor.PURPLE + "F" + cor.END}): ')).upper(),
                        telefone=int(input(cor.BOLD+ 'NÚMERO DE TELEFONE: ' + cor.END))
                    )]
                except ValueError:  # Caso o usuário digite algo que não deve
                    print(cor.BOLD + cor.RED + '\nINVÁLIDO!\n' + cor.END)
                else:
                    break
        elif escolha == 2:
            print(cor.YELLOW+'***********************************************************\n\t\t\t\tRelatório dos clientes\n***********************************************************'+cor.END)
            for i in range(len(usuario)):
                cliente.relatorio(usuario[i], i, cliente.difference(usuario[i], i))
        elif escolha == 3:
            while True:
                try:
                    id = int(input('ID do usuário: '))
                    for i in range(len(usuario)):
                        if id == usuario[i].id:
                            print(cor.YELLOW+'***********************************\n\t\tRelatório do cliente\n***********************************'+cor.END)
                            cliente.relatorio(usuario[i], i, cliente.difference(usuario[i], i))
                            break
                    else:
                        print(cor.BOLD+cor.RED+'ID não existente'+cor.END)
                    input('Pressione Enter para voltar ao menu principal...'); break
                except ValueError:
                    print('Valor não inteiro')
        else:
            print('\nSaindo...\n')
            break



