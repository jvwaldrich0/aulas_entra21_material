# Exercicio 2
# 
# Imprima o menu de uma aplicação de cadastro de pessoas
# 
# O menu deve conter as opções de Cadastrar, Alterar, listar pessoas, alem da opção sair
def pessoas(name):
    nome = str(name)
    return nome

# Variaveis
lista = []
i = 0
# Escolhas
while True:
    try:
        escolha = int(input(
    '''
    Escolha uma opção:
    1 - Cadastrar
    2 - Alterar cadastro
    3 - Listar pessoas
    APERTE QUALQUER OUTRO NUMERO PARA SAIR
    
    Escolha: '''))
        if escolha == 1:
            #Cadastro
            nome = str(input('Aperta a tecla 0(zero) para sair!\nDigite o nome da pessoa que você deseja cadastrar:'))
            if nome != str(0):
                lista += [str(i)+' - '+ nome]
                i += 1
        elif escolha == 2:
            #Alterar variavel
            print(*lista, sep='\n',)
            alterar = int(input('\nEscolha: '))
            if alterar != int('a'):
                lista[alterar] = str(str(alterar)+' - '+input('\nQual o novo nome? '))
        elif escolha == 3:
            #exibir lista
            print('\n',*lista, sep='\n')
        else:
            break
    except ValueError:
        #Caso o usuario digite algo errado
        print('\nVocê Digitou algo errado!')