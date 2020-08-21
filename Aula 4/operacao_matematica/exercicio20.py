#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

print('Software para calcula o valor total do emprestimo')
while True:
    try:
        tempo_emprestimo = int(input('Tempo de emprestimo(mês): '))
        taxa_juros = float(input('Taxa de juros(%): '))
        dinheiro_emprestado = float(input('Dinheiro emprestado = R$'))
        if tempo_emprestimo != 1:
            print(f'''
Valores:
    Dinheiro emprestado = R${dinheiro_emprestado}
    Taxa de juros = {taxa_juros:.1f}%
    Período de empréstimo = {tempo_emprestimo} meses

Valor a receber é igual a R${(float(dinheiro_emprestado * (1 + (taxa_juros / 100)) ** tempo_emprestimo)):.2f}
    ''')
        else:
            print(f'''
Valores:
    - Dinheiro emprestado = R${dinheiro_emprestado}
    - Taxa de juros = {taxa_juros:.1f}%
    - Período de empréstimo = {tempo_emprestimo} mês

Valor a receber é igual a R${(float(dinheiro_emprestado * (1 + (taxa_juros / 100)) ** tempo_emprestimo)):.2f}
            ''')
    except ValueError:
        #caso usuario tente escrever algo que não foi pedido
        print('\nVocê digitou algum número errado\n')
    else:
        #escolha de quebra do loop
        escolha = int(input('\nDigite 1 para reiniciar:'))
        if escolha != 1:
            break