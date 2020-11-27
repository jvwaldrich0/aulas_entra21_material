# Exercicio 2
# Faça um programa que peça um número.
# 
# Mostre na tela se este número é negativo ou positivo. (lembrando que números positivos são maiores que zero!)

print('Software que diz se o número é positivo ou negativo')
while True:
    try:
        num1 = int(input('Digite um número: '))
        if num1 > 0:
            print('\nNúmero Positivo!\n')
        elif num1 == 0:
            print('\nNúmero Neutro\n')
        else:
            print('\nNúmero Negativo\n')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break