"""Exercicio 09

Faça um programa que pegue uma lista de valores e separe em 2 listas. Uma com valores menores que 500.00 e
outra com maiores ou igual.

Depois motre o maior e o menor valor da cada lista.
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

vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00];vandas.sort()
menor = vandas[:6]
maior = vandas[6:]

while True:
    print(cor.BOLD+cor.YELLOW+'Lista Original: '+cor.END,vandas)
    print(cor.BOLD+cor.BLUE+f'\nMaior: {maior}\n'+cor.END,
          cor.BOLD+cor.GREEN+f'\nMenor: {menor}'+cor.END)
    escolha = int(input('\nDigite 1 para reiniciar: '))
    if escolha != 1:
        break

