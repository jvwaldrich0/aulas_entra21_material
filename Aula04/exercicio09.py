
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.

nome_cliente = input('Digite seu nome: ')
nome_produto = input('Digite o nome do produto: ')
quantidade = int(input('Quantidade do produto? '))
preco = float(input('Preço do produto? '))

total = preco + quantidade

print(nome_cliente+' acaba de comprar ',quantidade,nome_produto+' e pagou no total: R$',preco)