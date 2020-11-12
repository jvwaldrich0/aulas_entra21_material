
"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
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

notas = []

for i in range(10):
    while True:
        try:
            notas += [int(input(f'Digite a nota {i+1}: '))] # Input das notas
            while notas[i] > 10:
                print(cor.BOLD + cor.YELLOW+('\nVocê digitou um valor errado!\n'.upper() + cor.END))
                notas[i] = int(input(f'Digite a nota {i+1}: '))
            break
        except ValueError:
            print(cor.BOLD + (cor.YELLOW + '\nVocê digitou um valor errado!\n'.upper()) + cor.END)
else: #Após o loop
    if (sum(notas) / 10) >= 7:
        print(cor.BOLD + (cor.GREEN + '\nAprovado\n'.upper()+ cor.END))
    elif 5.5 < float(sum(notas) / len(notas)) < 7:
        print(cor.BOLD + (cor.YELLOW + '\nRecuperação\n'.upper()+ cor.END))
    elif 0 < float(sum(notas) / len(notas)) < 5.5:
        print(cor.BOLD + (cor.RED + '\nReprovado\n'.upper()+ cor.END))
