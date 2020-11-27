# Exercicio 10
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem decrescente.
#
list = []
print('Software que pede 3 números inteiros e mostre os três em ordem decrescente')
while True:
    try:
        # Esta fiz com lista, da para ver o quanto de linha economiza em relação a exercicio 09
        for i in range(3):
            list += [int(input('Digite um número: '))]
        list = sorted(list, reverse=True)
        print('\n',*list, sep='\n')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break