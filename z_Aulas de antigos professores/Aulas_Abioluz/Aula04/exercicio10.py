# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.
while True:
    try:
        # Variaveis produto 1
        produto1_nome = input('Nome do produto: ')
        produto1_quantidade = int(input('Quantidade: '))
        produto1_valor = float(input('Preço: '))
        #Variaveis produto 2
        produto2_nome = input('Nome do produto: ')
        produto2_quantidade = int(input('Quantidade: '))
        produto2_valor = float(input('Preço: '))
        #Calculo
        produto2_total = float(produto2_valor*produto2_quantidade)
        produto1_total = float(produto1_quantidade*produto1_valor)
        #Exibir na tela
        print(f'''
Nome: {produto1_nome}
Valor = R${produto1_valor:.2f}
Quantidade = {produto1_quantidade}
Total = R${produto1_total:.2f}

Nome: {produto2_nome}
Valor = R${produto2_valor:.2f}
Quantidade = {produto2_quantidade}
Total = R${produto2_total:.2f}
''')
    except ValueError:
        print('Você digitou algo errado!')
    else:
        escolha = int(input('Digite 1 para reiniciar: '))
        if escolha != 1:
            break