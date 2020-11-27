# **Exercícios**

# Dada a seguinte lista, resolva os seguintes questões:



# EXECUTE ESTE QUADRO PARA PODER USAR A LISTA
lista = [10, 20, 'amor', 'abacaxi', 80, 'Abioluz', 'Cachorro grande é de arrasar']


# 1) Usando a indexação, escreva na tela a palavra abacaxi

print(lista[3], sep='\n')




# 2) Usando a indexação, escreva na tela os seguintes dados: 20, amor, abacaxi


print(lista[1:4], sep=', ')



# 3) Usando a indexação, escreva na tela uma lista com dados de 20 até Abioluz
# 

print(lista[1:6])




# 4) Usando a indexação, escreva na tela os seguintes dados:
# 10, amor, 80, Cachorro grande é de arrasar


print(lista[::2])

# 5) Usando a indexação escreva na tela os seguintes dados:
# amor - 10 - 10 - abacaxi - Cachorro grande é de arrasar - Abioluz - 10 - 20

print(*(lista[2],lista[0]*2,lista[3],lista[6],lista[5],lista[0],lista[1]),sep=' - ')

# 6) Usando a indexação, escreva na tela uma lista com dados de 10 até 80

l = []
for i in range(81):
    l += [i]
print(l[10:81])


# 7) Usando a indexação, escreva na tela os seguintes dados:
# 10, abacaxi, Cachorro grande é de arrasar


print(lista[0],lista[3],lista[6], sep=', ')



