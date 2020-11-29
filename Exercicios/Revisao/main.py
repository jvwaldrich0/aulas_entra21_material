#!/bin/python3
from Exercicios import exercises as e


while True:
    try:
        for i in range(8):
            print(f'{i} - Exercicio {i}')
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
                pass
            elif escolha == 7:
                pass
            elif escolha == 8:
                pass
            elif escolha == 9:
                print('Saindo...')
                break
    except ValueError:
        print('Valor errado')
    except KeyboardInterrupt:
        print('Ate logo!')
    finally:
        e.clear()

