# Crie uma lista com todas as letras do alfabeto

# Remova as vogais dessa lista e crie uma tupla com elas

# Crie uma coleção com as letras do seu nome (utilizando a lista e a tupla, sem remover itens).
# depois, adicione sua idade e o nome do seu livro favorito

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h' ,'i' ,'j' ,'k' , 'l', 'm', 'n' ,'o' ,'p' ,'q' , 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vogal = []


contador = 0

for letra in alfabeto:
    if letra == 'a':
        vogal += alfabeto.pop(contador)
    if letra == 'e':
        vogal += alfabeto.pop(contador)
    if letra == 'i':
        vogal += alfabeto.pop(contador)
    if letra == 'o':
        vogal += alfabeto.pop(contador)
    if letra == 'u':
        vogal += alfabeto.pop(contador)
    contador += 1
else:
    vogal = tuple(vogal)

print(alfabeto, type(alfabeto))
print(vogal, type(vogal))