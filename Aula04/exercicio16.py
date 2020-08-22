# Exercicio 16
# Foi verificado que a venda de bermudas aumenta conforme aumenta a temperatura (t) (float) conforme a seguinte fórmula:
# 
# bermudas = 1.5t + t + 150
# 
# Lembrando que o t significa temperatura.
# 
# Faça um programa para o seu superior que peça a temperatura e mostre a venda prevista de bermudas.

#print
print('Um software que pede a temperatura e mostre a venda prevista de bermudas baseado na formula:\n\nbermudas = 1.5t + t + 150.\n\tt = temperatura\n')
#loop
while True:
    try:
        t = float(input(f'Digite a temperatura(°C): '))
        print(f'Valor da bermuda = R${(1.5*t + t + 150):.2f}')
    except ValueError:
        # caso usuario tente escrever algo que não foi pedido
        print('Você digitou a temperatura errado!')
    else:
        # escolha de quebra do loop
        escolha = int(input('Digite 1 para reiniciar: '))
        if escolha != 1:
            break