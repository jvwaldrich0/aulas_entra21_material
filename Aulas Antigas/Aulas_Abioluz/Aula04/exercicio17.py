# Exercicio 17
# A formula de calculo de área de um circulo é:
# 
# area = pi*r²
# 
# Sabemos que:
# 
# pi = 3.14
# r = raio da circunferência em metros (float)
# 
# Crie um programa que peça ao usuário o raio e calcule a área da circunferência

# importei a biblioteca de matemática
from math import pow

#print
print('Um programa que pede ao usuário o raio e calcule a área da circunferência')
while True:
    try:
        r = float(input('Quanto mede o raio: '))
        print(f'Área = {3.14*(pow(r,2))}')
    except ValueError:
        # caso usuario tente escrever algo que não foi pedido
        print('Você digitou algum número errado')
    else:
        # escolha de quebra do loop
        escolha = int(input('Digite 1 para reiniciar: '))
        if escolha != 1:
            break