# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.
# 
#
print('Software que pede 3 números inteiros e mostre os três em ordem crescente')
while True:
    try:
        #Esta fiz no if
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        n3 = int(input("Digite o último número: "))
        if (n1 >= n2):
            if (n2 >= n3):
                print(str(n3) + " " + str(n2) + " " + str(n1))
            elif (n1 >= n3):
                print(str(n2) + " " + str(n3) + " " + str(n1))
            else:
                print(str(n2) + " " + str(n1) + " " + str(n3))
        else:
            if (n3 >= n2):
                print(str(n1) + " " + str(n2) + " " + str(n3))
            elif (n3 >= n1):
                print(str(n1) + " " + str(n3) + " " + str(n2))
            else:
                print(str(n3) + " " + str(n1) + " " + str(n2))
    except ValueError:
        # Caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break
