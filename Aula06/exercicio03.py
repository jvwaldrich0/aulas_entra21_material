"""Execicios 03

Escreva um programa que contenha um menu com 4 opções:
A) soma
B) média
C) divisão
D) Sair

As opções podem ser escolhidas com as letras maiusculas ou minusculas.

Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.

Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.

Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"

Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"
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
class calc:
    def soma(self):
        while True:
            try:
                num1 = int(input('Digite algum número: '))
                num2 = int(input('Digite outro número: '))
            except ValueError:
                # caso o usuario digite um valor errado
                print(cor.BOLD + (cor.RED + '\nVocê digitou um valor errado!'.upper() + cor.RED) + cor.END, '\n')
            else:
                return print(cor.BOLD+'\nResultado:'+cor.END, num1+num2)
    def media(self):
        list = []
        while True:
            try:
                for i in range(4):
                    list += [int(input('Digite um número: '))]
                return print(cor.BOLD+'\nResultado:'+cor.END, float((list[0]+list[1]+list[2]+list[3])/4))
            except ValueError:
                # caso o usuario digite um valor errado
                print(cor.BOLD + (cor.RED + '\nVocê digitou um valor errado!'.upper() + cor.RED) + cor.END, '\n')
    def divisao(self):
        while True:
            try:
                num1 = int(input('Digite algum número: '))
                num2 = int(input('Digite outro número: '))
                quociente = float(num1/num2)
            except ValueError:
                # caso o usuario digite um valor errado
                print(cor.BOLD + (cor.RED + '\nVocê digitou um valor errado!'.upper() + cor.RED) + cor.END, '\n')
            except ZeroDivisionError:
                # Caso haja uma divisão por zero
                print(cor.BOLD + (cor.RED + '\nNão é possivel dividir por zero!'.upper() + cor.RED) + cor.END, '\n')
            else:
                return print(cor.BOLD+'\nResultado:'+cor.END, quociente)

c = calc()
while True:
    try:
        while True:
            menu = str(input('''
Desejo fazer;
A) soma
B) média
C) divisão
D) Sair

Escolha: '''))
            if menu.lower() == 'a' or 'b' or 'c' or 'd' :
                break
            else:
                print(cor.BOLD + (cor.RED + '\nVocê digitou uma letra não existente no menu!'.upper() + cor.RED) + cor.END, '\n')
        if menu.lower() == 'a':
            calc.soma(self=c)
        elif menu.lower() == 'b':
            calc.media(self=c)
        elif menu.lower() == 'c':
            calc.divisao(self=c)
        elif menu.lower() == 'd':
            print('Saindo...')
            break
    except ValueError:
        # caso o usuario digite um valor errado
        print(cor.BOLD + (cor.RED + '\nVocê digitou um valor errado!'.upper()+ cor.RED) + cor.END, '\n')