'''Execicios 01

Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições

Venda Total
de R$ 0.00 a R$ 30000.00 - 0%
de R$ 30000.01 a R$ 50000.00 - 1.5%
de R$ 50000.01 a R$ 100000.00 - 2.5%
Acima de R$ 100000.00 - 3.5%'''
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
        comissao = float(input('Quanto foi vendido: R$'))
        if 0 <= comissao <= 30000.00:
            print('Você recebera de comissão o valor de R$0,00')
        elif 30000.01 <= comissao <= 50000:
            print(f'Você reberá de comissão o valor de R${comissao*0.015}')
        elif 50000.01 <= comissao <= 100000:
            print(f'Você reberá de comissão o valor de R${comissao * 0.025}')
        elif 100000.01 <= comissao :
            print(f'Você reberá de comissão o valor de R${comissao * 0.025}')
        else:
            print((cor.BOLD+(cor.YELLOW+'\nNão aceitamos valores negativos!')+cor.END))
    except ValueError:
        # Caso o usuario digite um valor errado
        print(cor.BOLD + (cor.RED + '\nVocê digitou um caractere errado!'.upper() + cor.RED) + cor.END, '\n')
    else:
        escolha = int(input(cor.BOLD + (cor.RED + '\nDigite 1 para reiniciar: ') + cor.END))
        if escolha != 1:
            break