# Exercicio 11
# Escreva um programa que peça o peso (float) de 3 pessoas e motre na tela a soma de todos os pesos. 
while True:
    try:
        #Variaveis
        peso1 = float(input('Digite o peso 1 em Kg: '))
        peso2 = float(input('Digite o peso 2 em Kg: '))
        peso3 = float(input('Digite o peso 3 em Kg: '))
        #Soma
        soma = peso1 + peso2 + peso3
        #Exibir
        print(f'A soma de todos os pesos é igual a {soma:.3f}Kg')
    except ValueError:
        #Caso ocorra algum problema de digitação
        print('Você digitou algo errado!')
    else:
        #Repetição ou saida
        if int(input('Digite 1 para tentar novamente: ')) != 1:
            break
