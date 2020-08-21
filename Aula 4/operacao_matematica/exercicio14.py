
# Exercicio 14
# Crie um programa que solicite o valor de x (inteiro)
# 
# calcule usando a fórmula 2x+3
# 
# mostre o resultado

#print
print('Digite qualquer número para eu aplicar a fórmula 2x+3')
#loop
while True:
    try:
        x = int(input('X = '))
        print(f'a soma de 2*{x}+3 é igual a {2*x+3}')
    except ValueError:
        #caso usuario tente não escrever o que foi solicitado
        print('Você digitou algum número errado')
    else:
        #escolha de quebra ou não do loop
        escolha = int(input('Digite 1 para reiniciar: '))
        if escolha != 1:
            break