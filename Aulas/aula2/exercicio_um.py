# Crie uma lista com todas as letras do alfabeto
consoantes = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(consoantes)

# Remova as vogais dessa lista e crie uma tupla com elas
vogais = (consoantes.pop(consoantes.index("a")),consoantes.pop(consoantes.index("e")),consoantes.pop(consoantes.index("i")),
    consoantes.pop(consoantes.index("o")),consoantes.pop(consoantes.index("u")))
print(vogais)

# Crie uma coleção com as letras do seu nome (utilizando a lista e a tupla, sem remover itens).
# depois, adicione sua idade e o nome do seu livro favorito
colecao = {consoantes[0],  consoantes[10], consoantes[-8], vogais[-1], vogais[3]}
colecao.add(32)
colecao.add("Senhor do anéis, a sociedade do anel")

print(colecao)