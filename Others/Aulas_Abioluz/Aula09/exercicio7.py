"""Exercicio 07

Faça um programa que receba 10 idades e mostre a seguinte mensagem:

Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Psicina de bolinhas liberado
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
    idade = []
    for i in range(10):
        try:
            idade += [int(input(f'Digite a idade {i + 1}: '))]
        except ValueError:
            # --- Correção do erro de não inteiro em venda --- #
            print(cor.BOLD + (cor.YELLOW + '\nVocê digitou um valor errado!\n'.upper()) + cor.END)
            while True:
                try:
                    idade += [int(float(input(f'Redigite a idade {i + 1}: ')))]
                    if (type(idade[i]) == type(2)) and (idade[i] >= 0):
                        break
                except ValueError:
                    continue
            print(cor.BOLD + cor.CYAN + '\nMuito bem, vamos continuar...\n'.upper() + cor.END)
    else:
        for i in range(10):
            print(f'\nusuário {i+1} possui {idade[i]} anos portanto: '.upper())
            if idade[i] > 18:
                print(cor.BOLD+cor.GREEN+'Ingressos da Rave liberado!\n'+cor.END)
            elif 16 < idade[i] <= 18:
                print(cor.BOLD+cor.YELLOW+'Ingressos do cinema liberado\n'+cor.END)
            elif 13 < idade[i] <=16:
                print(cor.BOLD+cor.BLUE+'Ingreços para fliperama liberado\n'+cor.END)
            elif 0 <= idade[i] <= 13:
                print(cor.BOLD+cor.CYAN+'Piscina de bolinhas liberado\n'+cor.END)
    escolha = int(input('\nDigite 1 para reiniciar: '))
    if escolha != 1:
        break
