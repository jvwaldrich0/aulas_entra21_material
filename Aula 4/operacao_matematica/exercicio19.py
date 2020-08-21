# Exercicio 19
# Para calcular o valor do empréstimo usa-se a seguinte fórmula:

# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo

# Sendo que:
# valor_receber (float) -> É o valor que você deve receber de volta. Este valor é sempre maior que o valor emprestado.
# dinheiro_emprestado (float) -> É o valor que você está emprestando.
# taxa_juros (float) -> Essa é a taxa de juros em porcentagem que irá ser aplicado no valor emprestado todo o mês 
# aumentando o valor a receber
# tempo_emprestimo (inteiro) -> É o tempo que vai demorar para voê receber o dinheiro de volta.

# Se você emprestou R$150.00 por 3 mêses a uma taxa de 4.5 porcento ao mês, você deve fazer a seguinte conta:

# valor_receber = 150*(1+(4.5/100))**3

# o resultado deve ser: 171.17491874999996

# Crie um programa que calcule o emprestimo de R$250.00 a uma taxa de 5.5 porcento ao mês. 
# O programa deve pedir ao usuário que digite quantos mêses deve durar o empréstimo e mostre na tela o valor a ser recebido.

print('Software para calcula o valor total do emprestimo')
while True:
    try:
        tempo_emprestimo = int(input('Tempo de emprestimo(mês): '))
        print(f'\nValor a receber é igual a R${(float(250.00 * (1 + (5.5 / 100)) ** tempo_emprestimo)):.2f}')
    except ValueError:
        #caso usuario tente escrever algo que não foi pedido
        print('\nVocê digitou algum número errado\n')
    else:
        #escolha de quebra do loop
        escolha = int(input('\nDigite 1 para reiniciar:'))
        if escolha != 1:
            break