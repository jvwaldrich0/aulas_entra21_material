"""Exercício 1

(não usar o continue ou o break)

Crie um programa que mostre um memu com as seguites opções:

1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 númeors e mostre a subtração deles
Para númeor 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.

Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""


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
2) Subtração
3) Multiplicação
S) Para sair!

> ''')
    except ValueError:
        print('\nOpção Inválida\n')
    else:
        if escolha == '1':
            print('\nResultado = ', num(1) + num(2))
        elif escolha == '2':
            print('\nResultado = ', num(1) - num(2))
        elif escolha == '3':
            print('\nResultado = ', num(1) * num(2))
        else:
            if escolha.upper() != 'S': print('\nOpção Inválida\n')
else:
    print('\nSaindo...')