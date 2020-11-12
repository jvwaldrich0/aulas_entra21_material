
"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
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
    nome = []
    for i in range(10):
        try:
            nome += [f'Usuário {i+1}: '+cor.BOLD+cor.BLUE+str(input(f'Digite o nome do usuário {i + 1}: '))+cor.END]
        except ValueError:
            # --- Correção do erro de não inteiro em venda --- #
            print(cor.BOLD + (cor.YELLOW + '\nVocê digitou um valor errado!\n'.upper()) + cor.END)
    else:
        print('\n',*nome,'\n', sep='\n')
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break