"""
For e Listas

O uso do for como contador pode ser muito útil para sincronizar várias listas. 
Supondo que temos listas para armazenar vários dados diferentes de várias pessoas. Se as listas tiverem ordenada, onde o índice 0 de cada lista é o dado de uma pessoa, podemos recuperar os dados dos cadastros facilmente.

Para isso usamos o for como um contador e usamos a variável i para sincronizar todas as listas.
"""

# Faça um programa de cadastro de pessoas que receba 5 nomes, idades e e-mails e
# salve cada um em uma lista. Depois mostre os dados dos clientes.

################################################################################
#                          Captação de dados                                   #
################################################################################

# iniciando listas vazias para capturar dados dos clientes
lista_nomes = [ ]
lista_idades = [ ]
lista_email = [ ]

# Usando o for a nosso favor, para cadastrar novos clientes
for i in range(3):
    # Entrada dos dados
    nome = input(f'Digite o nome {1+i}: ' )
    idade = input(f'Digite o idade {1+i}: ' )
    email = input(f'Digite o email {1+i}: ' )
    # Adicionando os dados nas listas.
    lista_nomes.append( nome )
    lista_idades.append( idade )
    lista_email.append( email )
    print('\n')

# Até aqui tudo bem, foi o mais do mesmo!

################################################################################
#                      Apresentação dos resultados                             #
################################################################################

# Para sincronizarmos a lista, devemos pegar uma e medir o tamanho dela.
# Como eu sei que todas tem o mesmo tamanho, qualquer uma das listas de cadastro
# já é o suficiente.

tamanho = len( lista_nomes )

# Vamos usar o for como contador e colocar a variável tamanho dentro do range()
# Assim ela irá fazer o loop na medida certa para pegar-mos todos os dados 
# cadastrados.
for i in range( tamanho ): 
    # Printamos os resultados.
    print( f'''
nome: { lista_nomes[ i ] }
Idade: { lista_idades[ i ] }
E-mail: { lista_email[ i ] } 
''' )







