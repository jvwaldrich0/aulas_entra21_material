# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente

print('Software que compara dois números em ordem crescente')
while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número:'))
        if num1 > num2:
            print(f'''
1° {num1}
2° {num2}''')
        elif num1 == num2:
            print(f'''
1° {num1}''')
        else:
            print(f'''
1° {num2}
2° {num1}''')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break