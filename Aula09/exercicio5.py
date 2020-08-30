"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. Cadastre cada venda separadaemnte
e depois mostre a média e o valor total vendido no dia.
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
        total = int(input('Digite quantas vendas você fez: '))
        venda = []
        for i in range(total):
            try:
                venda += [int(input(f'Digite a venda {i+1}: '))]
            except ValueError:
                # --- Correção do erro de não inteiro em venda --- #
                print(cor.BOLD + (cor.YELLOW + '\nVocê digitou um valor errado!\n'.upper()) + cor.END)
                while True:
                    try:
                        venda += [int(float(input(f'Redigite a venda {i+1}: ')))]
                        if type(venda[i]) == type(2):
                            break
                    except ValueError:
                        continue
                print(cor.BOLD + cor.CYAN + '\nMuito bem, vamos continuar...\n'.upper() + cor.END)
        else:
            print(f'\nO total de vendas foi: R${sum(venda)}\nA média é igual a R${sum(venda)/total}')
    except ValueError:
        print(cor.BOLD + (cor.YELLOW + '\nVocê digitou um valor errado!\n'.upper()) + cor.END)
    else:
        break