# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o numero 1 e domingo é 7.
while True:
    try:
        day = int(input('digite um número de 1 a 7: '))
        if day == 1:
            print('Segunda-feira')
        elif day == 2:
            print('Terça-feira')
        elif day == 3:
            print('Quarta-feira')
        elif day == 4:
            print('Quinta-feira')
        elif day == 5:
            print('Sexta-feira')
        elif day == 6:
            print('Sábado')
        elif day == 7:
            print('Domingo')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um número errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break