'''Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Taboada
S) Sair


Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a taboada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida"
'''

def num(i):
        while True:
            try:
                return int(input(f'Digite o número {i} > '))
            except ValueError:
                print('\nDigito errôneo\n')

escolha = '1'

while escolha.upper() != 'S':
    try:
        escolha = input('''
1) Soma
2) Media
3) Taboada
S) Para sair!

> ''')
    except ValueError:
        print('\nOpção Inválida\n')
    else:
        if escolha == '1':
            print('\nResultado = ', num(1) + num(2))
        elif escolha == '2':
            print('\nResultado = ', (num(1) + num(2) + num(3) + num(4))/4)
        elif escolha == '3':
           mult = num(1)
           for i in range(11):
               print(f'{mult} * {i} = {mult*i}')
        else:
            if escolha.upper() != 'S':print('\nOpção Inválida\n')
else:
    print('\nSaindo...')