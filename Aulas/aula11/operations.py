import sqlite3

conn = sqlite3.connect('poke.db')
cursor = conn.cursor()

# nome = input("digite o nome do treinador: ")
# idade = input("digite a idade do treinador: ")
# cidade = input("digite a cidade do treinador: ")

# cursor.execute("""
# INSERT INTO treinadores (nome, idade, cidade)
# VALUES (?,?,?)
# """, (nome, idade, cidade))
# conn.commit()

# cursor.execute("SELECT id from treinadores where nome = ?", [nome])
# id_treinador = cursor.fetchone()[0]

# cursor.execute("SELECT id, nome from pokemons")
# result_set = cursor.fetchall()

# msg = "Escolha seu pokemon inicial!\n"
# for pokemon in result_set:
#     msg += f"{pokemon[0]} - {pokemon[1]}\n" 

# id_pokemon = input(msg)

# cursor.execute("""
# INSERT INTO pokemons_treinador (id_treinador, id_pokemon)
# VALUES (?,?)
# """, (id_treinador, id_pokemon))
# conn.commit()

cursor.execute("""
    SELECT treinadores.nome, pokemons.nome from treinadores 
    INNER JOIN pokemons_treinador  ON treinadores.id = pokemons_treinador.id_treinador
    INNER JOIN pokemons ON pokemons_treinador.id_pokemon = pokemons.id
    WHERE treinadores.id = 1
    """)
    
result = cursor.fetchall()
print(result)

#print(f"Seja bem vindo ao mundo pokemon, {result[0][0]}! Cuide bem do seu {result[0][1]}!")


