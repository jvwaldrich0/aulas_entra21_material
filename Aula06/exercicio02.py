'''Escreva um programa que receba 4 notas e calcule a média.
Mostre a seguinte mensagem conforme a media final.

Media Final
de 0 a 5 - Reprovado
de 5 a 6.5 - Recuperação
de 6.5 a 9 - Aprovado
Acima de 9 - Aprovado com louvor'''

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

nota =[] # Ao invés de eu criar uma variável para cada nota, achei plausível criar uma variável composta com o nome de nota
while True:
    try:
        for i in range(4):
            nota += [float(input('Digite a nota: '))]
            # Evitar notas negativas ou acima de 10
            while True:
                if float(nota[i]) < 0:
                    print(cor.BOLD+(cor.RED+'\nNão é permito nota abaixo de 0!\n'.upper())+cor.END)
                    nota[i] = float(input('Digite sua nota: '))
                elif float(nota[i]) > 10:
                    print(cor.BOLD+(cor.RED+'\nNão é permito nota acima de 10!\n'.upper())+cor.END)
                    nota[i] = float(input('Digite sua nota: '))
                else:
                    break
        # Para não precisar criar outra variavel para media, peço ao interpretador do Python para que faça o calculo de antemão
        if ((nota[0]+nota[1]+nota[2]+nota[3])/4) > 9:
            print(cor.BOLD+(cor.GREEN+'\nAprovado com louvor!\n'.upper())+cor.END)
        elif 6.5 < ((nota[0]+nota[1]+nota[2]+nota[3])/4) <= 9:
            print('\nAprovado!\n'.upper())
        elif 5 < float((nota[0]+nota[1]+nota[2]+nota[3])/4) <= 6.5:
            print(cor.BOLD+(cor.YELLOW+'\nRecuperação!\n'.upper())+cor.END)
        else:
            print(cor.BOLD+(cor.RED+'\nReprovado!\n'.upper())+cor.END)
    except ValueError:
        # caso o usuario digite um valor errado
        print(cor.BOLD + (cor.YELLOW + '\nVocê digitou um valor errado!'.upper()+ cor.RED) + cor.END, '\n')
        print(cor.BOLD + (cor.RED + 'Redefina todas as notas novamente!'.upper()+ cor.RED) + cor.END, '\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break