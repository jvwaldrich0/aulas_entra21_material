# Exercicio 3
# Faça um programa que peça a idade do cliente.
# 
# Se ele tiver 18 anos ou mais deve aparecer a mensagem "Entrada permitida"
# 
# Caso contrário deve aparecer a mensagem "Entrada Negada!"

print('Software que analisa a idade do usuario')
while True:
    try:
        idade = int(input('Digite sua idade: '))
        if idade >= 18:
            print('Entrada Permitida')
        else:
            print('Entrada Negada!')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break