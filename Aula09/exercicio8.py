"""Exercicio 08
Faça um programa que pegue a lista e calcule a seguinte formula: 32x+125

Com o resultado desta formula mostre sómente os resultados maiores que 550.
Para os resultados menores que 550 mostre "número invalido!"
"""
lista = [1, 6, 9, 1, 5, 4, 8, 9, 15, 23, 14, 54, 82, 91, 45]
while True:
    print(lista)
    for i in range(len(lista)):
        if (lista[i]*32+125) >= 550:
            print(f'\nf({lista[i]}):32*{lista[i]}+125 = {lista[i]*32+125}')
        else:
            print('\nNúmero Inválido!'.upper())
    escolha = int(input('\nDigite 1 para reiniciar: '))
    if escolha != 1:
        break