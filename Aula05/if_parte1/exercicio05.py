# Exercicio 5
# Faça um programa que peça uma senha ao usuário.
# 
# Se a senha for igual a "Abacaxi" deve aparecer a mensagem "Entrada liberada"
# 
# Caso contrário deve aparecer a mensagem "Senha incorreta"

print('Software que analisa a senha do usuario(senha=Abacaxi)')
while True:
    try:
        senha = input('Digite sua senha: ')
        if senha == 'Abacaxi':
            print('Entrada liberada')
        else:
            print('Senha Incorreta')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break