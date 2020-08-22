
# Exercicio 15
# Crie um programa que solicite o valor de x (inteiro)
# 
# calcule usando a fórmula 3x-x+3
# 
# mostre o resultado

#print
print('Digite qualquer número para eu aplicar a fórmula 3x-x+3')
#loop
while True:
    try:
        x = int(input('X = '))
        print(f'a soma de 3*{x}-{x}+3 é igual a {(3*x)-x+3}')
        #resultado
    except ValueError:
        #caso usuario tente escrever algo que não foi pedido
        print('Você digitou algum número errado')
    else:
        #escolha de quebra do loop
        escolha = int(input('Digite 1 para reiniciar: '))
        if escolha != 1:
            break