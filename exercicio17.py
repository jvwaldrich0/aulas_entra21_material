# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"
#

#Adicionei umas cores para ficar mais bonito
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
        if ((nota[0]+nota[1]+nota[2]+nota[3])/4) == 10:
            print(cor.BOLD+(cor.GREEN+'\nAprovado com louvor!\n'.upper())+cor.END)
        elif 10 > ((nota[0]+nota[1]+nota[2]+nota[3])/4) >= 7:
            print('\nAprovado!\n'.upper())
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
