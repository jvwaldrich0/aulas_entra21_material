# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.

print('Software que pede 3 números inteiros e mostre o menor número')
while True:
    try:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número:'))
        num3 = int(input('Digite o ultimo número: '))
        list = [num1,num2,num3]; list = sorted(list)
        print(f"{list[0]} é o menor", sep='\n' )
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break




