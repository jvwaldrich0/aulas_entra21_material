# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

def produtos:
    nome = input('Nome: ')
    preco = float(input('Valor: '))
    quantidade = int(input('Quantidade: '))
    def total(preco,quantidade):
        return (float(preco) * float(quantidade))
    def name(nome):
        return nome

produto1 = input('Nome: ')
produto2 = input('Nome: ')
