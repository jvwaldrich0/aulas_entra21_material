# Exercicio 1
# 
# Faça um programa que peça 2 numeros inteiros e mostre o maior deles.
# 
#

print('Software que compara dois números')
while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número:'))
        if num1 > num2:
            print(f'O maior número é o {num1}\n')
        elif num1 == num2:
            print(f'Os dois números são iguais!\n')
        else:
            print(f'O maior número é o {num2}\n')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break