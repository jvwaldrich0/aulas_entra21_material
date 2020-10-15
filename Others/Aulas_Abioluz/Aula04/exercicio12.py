# Exercicio 12
# 
# Crie um program que peça ao usuário que digite 2 números reias(float) e mostre:
# 
# A soma dos dois
# A multiplicação dos dois
# A divisão do primeiro com o segundo
# A subtração dos dois

#print
print('Este software é um software de soma de dois números reais')
#loop
while True:
    try:#tente
        num1 = float(input('\nDigite um número real: '))
        num2 = float(input('\nDigite outro número real: '))
        print(f'O resultado da soma é {num1+num2}')
        #resultado
    except ValueError:
        #Caso o usuario tente escrever algum numero não real
        print('\nVocê digitou algo errado!\n')
    else:
        #escolha
        escolha = int(input('Digite 1 para reiniciar: '))
        if escolha != 1:
            #caso escolha diferente de 1 ele quebra o loop
            break