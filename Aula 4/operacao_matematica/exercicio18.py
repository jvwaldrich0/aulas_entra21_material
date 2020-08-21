# Exercicio 18
# Crie um programa que solicite o valores (inteiros) de a, b e c para o cálculo do delta
# 
# A fórmula do delta é:
# 
# delta = b²-4ac
# 
# após calcular, mostre o resultado na tela.
from math import pow

print('Software para calcula do delta')
while True:
    try:
        print('Irei pedir alguns valores a você para o calculo do Delta ok?')
        a = int(input('a = '))
        b = int(input('b = '))
        c = int(input('c = '))
        #resultado
        print(f'O seu resultado foi {(pow(b,2)-(4*a*c))}')
    except ValueError:
        #caso usuario tente escrever algo que não foi pedido
        print('Você digitou algum número errado')
    else:
        #escolha de quebra do loop
        escolha = int(input('Digite 1 para reiniciar: '))
        if escolha != 1:
            break