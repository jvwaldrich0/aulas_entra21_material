
# Calcule o valor total dos itens e aplique descontos:

# se o valor for superior a 100, 2% de desconto
# se o valor for superior a 200, 5% de desconto
# se o valor for superior a 500, 10% de desconto

# descubra qual o item mais caro da lista

# ordene os itens da lista por ordem alfabética
def menu():
    return f'''
{traco()} Carinho {traco()}
1 - Adicionar um produto
2 - Listar todos os produtos cadastrados
3 - Confirmar comprar
{traco()}---------{traco()}'''

def traco():
    return '-' * 8


total = float(0)
precos = []
produtos = []

try:
    while True:
        print(menu())
        escolha = int(input('> '))
        if escolha == 1:
            produtos += [input('Nome do produto: ').upper()]
            precos += [float(input('Valor do produto: '))]
        elif escolha == 2:
            for i in range(len(precos)):
                print(f'{produtos[i]} = R${precos[i]:.2f}')
        elif escolha == 3:
            print('\nCalculando algum desconto...')
            total = sum(precos)
            break
except ValueError:
    print('Valor não aceito!')
else:
    total1 = total
    if 200 > total > 100:
        a = '2%'
        total = total * 0.98
    elif 500 > total > 200:
        a = '5%'
        total = total * 0.95
    elif total > 500:
        a = '10%'
        total = total * 0.9
    else:
        a = '0%'
        print('\nNenhum desconto aplicado ;/\n')
    produtos.sort()
    precos.sort(reverse=True)
finally:
    print(*produtos, f'''
Total = R${total1:.2f}
Desconto: {a}
Total + Desconto = R${total:.2f}

OBS:
    -> Item mais caro esta valendo R${precos[0]:.2f}
''', sep='\n')
