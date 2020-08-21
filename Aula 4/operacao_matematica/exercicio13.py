# Exercicio 13
# Crie um programa que solicite o valor de x (inteiro)
# 
# calcule usando a fórmula x+3
# 
# mostre o resultado

#print
print('Digite qualquer número para eu somar 3')
#loop
while True:
    try:
        x = int(input('X = '))
        print(f'a soma de {x}+3 é igual a {x+3}')
    except ValueError:
        #caso o usuario tente escrever algo fora do solicitado
        print('Você digitou algum número errado')
    else:
        #quebra ou não do loop
        escolha = int(input('Digite 1 para refazer: '))
        if escolha != 1:
            break