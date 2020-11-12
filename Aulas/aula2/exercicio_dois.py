# Crie uma lista de compras com 10 produtos e seus preços
compras = {
    "arroz" : 30,
    "feijão" : 10,
    "macarrão": 5,
    "batata": 3,
    "trigo": 12,
    "oleo": 7,
    "picanha": 50
}
print(compras)

# Calcule o valor total dos itens e aplique descontos:
total = sum(compras.values())
print(total)
if (total > 100):
    print(total-(total*0.02))
elif (total > 200):
    print(total-(total*0.05))
elif (total > 500):
    print(total-(total*0.1))
# se o valor for superior a 100, 2% de desconto
# se o valor for superior a 200, 5% de desconto
# se o valor for superior a 500, 10% de desconto

# descubra qual o item mais caro da lista
print(max(compras, key=compras.get))

dicionario_ordenado = {k : compras[k] for k in sorted(compras)}
print(dicionario_ordenado)