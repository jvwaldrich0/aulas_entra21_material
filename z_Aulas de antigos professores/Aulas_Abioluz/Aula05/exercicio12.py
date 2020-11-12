# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

from math import pow as p

print('Software que pede 2 números inteiros e mostre um menu interativo contendo 5 operações matemáticas do python')
while True:
    try:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número:  '))
        operacao = int(input('''
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potênciação

Escolha: '''))
        if operacao == 1:
            print(f'{num1}+{num2} = {num1+num2}')
        elif operacao == 2:
            print(f'\n{num1}-{num2} = {num1-num2}\n{num2}-{num1} = {num2-num1}\n')
        elif operacao == 3:
            print(f'\n{num1}*{num2} = {num1*num2}')
        elif operacao == 4:
            print(f'\n{num1}/{num2} = {num1 / num2}\n{num2}/{num1} = {num2 / num1}\n')
        elif operacao == 5:
            print(f'\n{num1}^{num2} = {p(num1,num2)}\n{num2}^{num1} = {p(num2,num1)}\n')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break
