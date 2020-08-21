
# Exercicio 11
# Faça um programa que peça o sexo do cliente. 
# 
# Se o cliente digitar 'F' deve aparecer a mensagem "Como você está bonita hoje!"
# 
# Se o cliente digitar 'M' deve aparecer a mensagem "Como você está forte? andou malhando?"
# 
# Se o cliente digitar qualquer outra coisa, deve aparecer a mensagem: "opção invalida!"
#

print('Software que pede o sexo do cliente')
while True:
    sexo = format(str(input('Digite um a letra referente ao seu sexo(M=Masculino,F=Feminino: '))).lower()
    if sexo == 'm':
        print('\nComo você está forte? andou malhando?')
    elif sexo == 'f':
        print('\nComo você está bonita hoje!')
    else:
        print(format('\nOpção Inválida!\n').upper())
    escolha = int(input('\nDigite 1 para reiniciar: '))
    if escolha != 1:
        break