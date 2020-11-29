#!/bin/python3
from Exercicios import exercises as e
from Exercicios.Poker.main import main as poker


while True:
    try:
        for i in range(8):
            print(f'{i+1} - Exercicio {i+1}')
        else:
            print('9 - Sair')
            escolha = int(input('> '))
            if escolha == 1:
                e.exercicio1()
            elif escolha == 2:
                e.exercicio2()
            elif escolha == 3:
                e.exercicio3()
            elif escolha == 4:
                e.exercicio4()
            elif escolha == 5:
                e.exercicio5()
            elif escolha == 6:
                e.exercicio6()
                print('\n')
            elif escolha == 7:
                e.exercicio7()
            elif escolha == 8:
                poker()
            elif escolha == 9:
                print('Saindo...')
                break
    except ValueError:
        print('Valor errado')
    except KeyboardInterrupt:
        print('Ate logo!')
    finally:
        e.clear()

