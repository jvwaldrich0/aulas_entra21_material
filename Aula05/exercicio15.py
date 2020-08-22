# Exercicio 15
# Crie um programa que peça ao usuário que digite um número de 1 a 12 e mostre o mês correspondente ao número.
# 
while True:
    try:
        while True:
            day = int(input('Digite um número de 1 a 12: '))
            if day == 1:
                print('Janeiro')
                break
            elif day == 2:
                print('Fevereiro')
                break
            elif day == 3:
                print('Março')
                break
            elif day == 4:
                print('Abril')
                break
            elif day == 5:
                print('Maio')
                break
            elif day == 6:
                print('Junho')
                break
            elif day == 7:
                print('Julho')
                break
            elif day == 8:
                print('Agosto')
                break
            elif day == 9:
                print('Setembro')
                break
            elif day == 10:
                print('Outubro')
                break
            elif day == 11:
                print('Novembro')
                break
            elif day == 12:
                print('Dezembro')
                break
            else:
                continue
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um número errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break