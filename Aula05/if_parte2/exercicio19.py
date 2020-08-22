# Exercicio 19
# Faça um programa para calcular a fórmula do bhaskara para equação de segundo grau: ax²+bx+c
# 
# Peça para o usuário digitar os valores de a, b e c
# 
# Calcule o delta "delta = (b**2)-(4*a*c)"
# 
# Se o delta der negativo, então deve aparecer a seguinte mensagem: "Delta negativo! Equação não pode ser resolvida!"
# 
# Se o delta for igual a zero, use esta fórmula "x=-b/(2*a)" e mostre o valor de x
# 
# Se delta for maior que zero, então use estas 2 fórmulas "x =(-b+(delta**(1/2)))/(2*a)" e "x2=(-b-(delta**(1/2)))/(2*a)"
# e mostre o os valores de x1 e x2
# ________________
# Nota: 
# Para testar se seu programa está certo use estes valores para a, b e c
# delta negativo a=1, b=1, c=1
# delta zero a=1, b=2, c=1
# delta positivo a=1, b=4, c=1

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
class calculo:
    def x1(self,b,delta,a):
        return (-b+(delta**(1/2)))/(2*a)
    def x2(self,b,delta,a):
        return ((-b - (delta ** (1 / 2))) / (2 * a))
    def zero(self,b,a):
        return ((-b / (2 * a)))

while True:
    try:
        print ('\nDigite os valores para verificar o estado o delta;')
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))
        delta = ((b**2)-(4*a*c))
        if delta > 0:
            #Parece um pouco grande mas eu adicionei algumas cores, chamei as funções de calculo que eu havia criado acima
            print(f'\nx1 = {cor.BOLD+(cor.BLUE+str(int((calculo.x1(a=a,b=b,delta=delta,self=calculo())))))+cor.END}\nx2 = {cor.BOLD+(cor.RED+str(int((calculo.x2(a=a,b=b,delta=delta,self=calculo())))))+cor.END}')
        elif delta == 0:
            print(f'\nx = {cor.BOLD+(cor.BLUE+str(int((calculo.zero(a=a,b=b,self=calculo())))))+cor.END}')
        else:
            print(cor.BOLD+(cor.RED+'\nDelta negativo! Equação não pode ser resolvida!')+cor.END)
    except ValueError:
        # Caso o usuario digite um valor errado
        print(cor.BOLD + (cor.RED + '\nVocê digitou um valor errado!'.upper() + cor.RED) + cor.END, '\n')
    else:
        escolha = int(input(cor.BOLD+(cor.YELLOW+'\nDigite 1 para reiniciar: ')+cor.END))
        if escolha != 1:
            break