# Exercicio 3
# 
# Crie 3 variáveis
# 
# Cada variável deve conter um número
# 
# Imprima na tela a soma dos 3 números

while True:
    try:
        #variaveis
        var1 = int(input('Digite a variavel 1: '))
        var2 = int(input('Digite a variavel 2: '))
        var3 = int(input('Digite a variavel 3: '))
        #Exibir o resultado da soma
        print(var1+var2+var3)
    except ValueError:
        #Caso o usuario digite algum valor que nao seja inteiro recebera esta mensagem
        print('\nVocê digitou algo errado!\n')
        continue
    else:
        #Escolha do usuario caso ele queira repetir o processo
        escolha = int(input('Digite 1 para fazer a soma das três variaveis novamente?'))
        if escolha == 1:
            print('\n')
            continue
        else:
            break