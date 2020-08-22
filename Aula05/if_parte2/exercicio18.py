# Exercicio 18
# Peça para o usuário digitar os valores de a, b e c
# 
# Calcule o delta "delta = (b**2)-(4*a*c)"
# 
# Se o delta der negativo, então deve aparecer a seguinte mensagem: "Delta negativo! Equação não pode ser resolvida!"
# 
# Se o delta der igual a zero, então deve aparecer a seguinte mensagem: "Delta igual a zero!"
# 
# Se o delta der positivo, então deve aparecer a seguinte mensagem: "A equação pode ser resolvida!"

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
        print ('Digite os valores para verificar o estado o delta;')
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))
        if ((b**2)-(4*a*c)) > 0:
            print(cor.BOLD+(cor.GREEN+'\nA equação pode ser resolvida!')+cor.END)
        elif ((b**2)-(4*a*c)) == 0:
            print(cor.BOLD+(cor.YELLOW+'\nDelta igual a zero!')+cor.END)
        else:
            print(cor.BOLD+(cor.RED+'\nDelta negativo! Equação não pode ser resolvida!')+cor.END)
    except ValueError:
        # caso o usuario digite um valor errado
        print(cor.BOLD + (cor.RED + '\nVocê digitou um valor errado!'.upper() + cor.RED) + cor.END, '\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break