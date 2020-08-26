import random

# 2) Crie uma lista com 10 números qualquer.

# Usando as funções da lista responda:

# Quantos itens tem a lista?
# Qual é o número maior?
# Qual é o número menor?
# Qual é o resultado da soma da lista?

while True:
    # ------------- Criar lista vazia
    lista = []
    # ------------- Gerador de lista pseudo aleatória
    for i in range(10):
        lista += [random.randint(1, 50)]
    # ------------- Organizar a lista
    lista.sort(reverse=True)
    # ------------- print da lista
    print(*lista, sep=' - ')
    # ------------- print do que foi solicitado acima
    print(f'''
Quantos itens tem a lista: {len(lista)}
Número maior: {lista[0]}
Número menor: {lista[9]}
Qual é o resultado da soma da lista: {sum(lista)}
''')
    while True:
        try:
            escolha = int(input('Digite 1 para reiniciar: '))
        except ValueError:
            print('\nDigite um número inteiro\n')
        else:
            break
    if escolha != 1:
        break