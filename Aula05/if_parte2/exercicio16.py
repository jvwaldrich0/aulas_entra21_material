# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 
while True:
    try:
        #------------------------ Não permitir outro valor além de 1,2 ou 3
        while True:
            tipo = int(input('Qual tipo de gasolina você deseja?\n1 - Gasolina\n2 - Diesel\n3 - Álcool\n\nEscolha: '))
            if tipo != (1 or 2 or 3):
                print('\nValor Inválido!\n'.upper())
            else:
                break
        #--------------------------- Não permitir valor negativo
        while True:
            qnt = float(input('Quantos litros você deseja abastecer?'))
            if qnt < 0:
                print('\nValor Inválido!\n'.upper())
            else:
                break
        #------------------------------ Sequencia de if -----------------------------------------
        if tipo == 1:
            if qnt > 20:
                print('Você escolheu mais de 20L de gasolina, portanto tem o desconto de 10%')
            elif qnt == 20:
                print('Você escolheu 20L de gasolina, portanto tem o desconto de 0%')
            else:
                print('Você escolheu menos de 20L de gasolina, portanto tem o desconto de 0%')
        elif tipo == 2:
            if qnt > 10:
                print('Você escolheu mais de 10L de diesel, portanto tem o desconto de 5%')
            elif qnt == 10:
                print('Você escolheu 10L de diesel, portanto tem o desconto de 1,5%')
            else:
                print('Você escolheu menos de 10L de diesel, portanto tem o desconto de 1,5%')
        elif tipo == 3:
            if qnt > 10:
                print('Você escolheu mais de 10L de álcool, portanto tem o desconto de 10%')
            elif qnt == 10:
                print('Você escolheu 10L de álcool, portanto tem o desconto de 5%')
            else:
                print('Você escolheu menos de 10L de álcool, portanto tem o desconto de 5%')
        #---------------------------------------------------------------------------------------
    except ValueError:
        #Caso o usuario digite algum valor errado
        print('\nVocê digitou um algo errado, tente novamente\n')
    else:
        #Reiniciar
        escolha = int(input('\nDigite 1 para reiniciar: '))
        if escolha != 1:
            break