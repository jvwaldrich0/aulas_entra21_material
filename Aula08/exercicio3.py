# 3) Estas 3 listas:
# 
vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%
#
print(f'''Armando:
    - Média: R${int(float(sum(vendas_armando)/6))}
    - Total de venda: R${sum(vendas_armando)}
    - Quantidade de vendas: {len(vendas_armando)}
    - Comissão: R${int(sum(vendas_armando)*0.015)}
Paulo:
    - Média: R${int(sum(vendas_paulo)/8)}
    - Total: R${sum(vendas_paulo)}
    - Quantidade de vendas: {len(vendas_paulo)}
    - Comissão: R${int(sum(vendas_paulo)*0.3)}
Eduardo:
    - Média: R${int(sum(vendas_eduardo)/5)}
    - Total de venda: R${sum(vendas_eduardo)}
    - Quantidade de vendas: {len(vendas_eduardo)}
    - Comissão: R${int(sum(vendas_eduardo)*0.02)}
''')