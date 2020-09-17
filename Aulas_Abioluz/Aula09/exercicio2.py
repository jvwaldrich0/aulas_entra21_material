
"""Exercicio 02

Faça um programa que mostre a tabuada de 1, 2, 3 e 4
"""
def tabuada(n):
    tabuada = []
    for y in range(0,11):
        tabuada += [n * y]
    return  tabuada
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

print(cor.BOLD+cor.BLUE+'Tabuada do 1 : '+str(tabuada(1)).replace('[',' ')[:33]+cor.END,
      cor.BOLD+cor.PURPLE+'Tabuada do 2 : '+str(tabuada(2)).replace('[',' ')[:38]+cor.END,
      cor.BOLD+cor.RED+'Tabuada do 3 : '+str(tabuada(3)).replace('[',' ')[:39]+cor.END,
      cor.BOLD+cor.YELLOW+'Tabuada do 4 : '+str(tabuada(4)).replace('[',' ')[:40]+cor.END,
      sep='\n' );input('\nAperte qualquer tecla para fechar: ')


