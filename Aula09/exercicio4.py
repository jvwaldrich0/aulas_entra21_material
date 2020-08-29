"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
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
# --- Variables --- #
nome = []
idade = []
email = []
# --- Info --- #
print(cor.BOLD+cor.YELLOW+'Irei fazer 10 cadastros\n\nOBS: Este software não possui filtro de e-mail,nome ou idade.\n'.upper()+cor.END)
# --- Loop --- #
for i in range(10):
    while True:
        try:
            nome += [input('Digite seu nome: ')]
            idade += [int(input('Digite sua idade: '))]
            email += [input('Digite seu email: ')]
            print(cor.BOLD + cor.RED + f'\nMais uma vez, falta somente {9 - i}\n'.upper() + cor.END)
            break
        except ValueError:
            # --- Correção do erro de não inteiro em idade--- #
            print(cor.BOLD + (cor.YELLOW + '\nVocê digitou um valor errado!\n'.upper()) + cor.END)
            while True:
                try:
                    idade += [int(float(input('Redigite sua idade: ')))]
                    if type(idade[i]) == type(2):
                        break
                except ValueError:
                    continue
            print (cor.BOLD+cor.CYAN+'\nMuito bem ,vamos continuar...\n'.upper()+cor.END)
else:
    #  ---- Loop of results
    for x in range(10):
        print(f'\n{cor.BOLD+cor.BLUE+f"Cadastro {x}:".upper()+cor.END}\n\nnome: {nome[x]}\nidade: {idade[x]}\nemail: {email[x]}\n')