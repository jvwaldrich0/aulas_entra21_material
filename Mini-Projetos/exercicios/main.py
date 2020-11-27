from Exercicios import ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8

while True:
    try:
        for i in range(8):
            print(f'{i} - Exercicio {i}')
        else:
            print('9 - Sair')
            escolha = int(input('> '))

            if escolha == 1:
                ex1.exercicio1()
            elif escolha == 2:
                ex2.exercicio2()
            elif escolha == 3:
                pass
            elif escolha == 4:
                pass
            elif escolha == 5:
                pass
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