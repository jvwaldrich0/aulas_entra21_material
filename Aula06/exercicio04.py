"""Execicios 04
Exercicio retirado do site <https://wiki.python.org.br/EstruturaDeDecisao>

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

Triângulo Equilátero: três lados iguais;

Triângulo Isósceles: quaisquer dois lados iguais;

Triângulo Escaleno: três lados diferentes;
"""
class cor:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

while True:
    try:
        a = float(input('Primeiro lado: '))
        b = float(input('Segundo  lado: '))
        c = float(input('Terceiro lado: '))
        if (a + b < c) or (a + c < b) or (b + c < a):
            print(cor.BOLD + (cor.RED + '\nNao é um Triângulo'.upper() + cor.RED) + cor.END, '\n')
            print('\nNao é um triângulo')
        elif (a == b) and (a == c):
            print(cor.BOLD + (cor.BLUE + '\nTriângulo Equilatero'.upper() + cor.RED) + cor.END, '\n')
        elif (a == b) or (a == c) or (b == c):
            print(cor.BOLD + (cor.BLUE + '\nTriângulo Isósceles'.upper() + cor.RED) + cor.END, '\n')
        else:
            print(cor.BOLD + (cor.BLUE + '\nTriângulo Escaleno'.upper() + cor.RED) + cor.END, '\n')
    except ValueError:
        # caso o usuario digite um valor errado
        print(cor.BOLD + (cor.YELLOW + '\nVocê digitou um valor errado!'.upper()+ cor.RED) + cor.END, '\n')
    else:
        escolha = int(input(cor.BOLD + (cor.YELLOW + '\nDigite 1 para reiniciar: '.upper()+ cor.RED) + cor.END))
        if escolha != 1:
            break