"""Exercício 3

(use somente o while)

Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

Para mairores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.

Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""

nome  = []
i = 0

while True:
    nome += [input('Digite seu nome: ').upper()]
    if nome == '':
        print('\nNome em branco\n')
        continue
    try:
        idade = int(input('Digite sua idade: '))
    except ValueError:
        print('\nObrigado pela preferência!\n')
        break
    else:
        if 0 < idade <= 18:
            print('Entrada Proibida.')
            nome.pop()
        else:
            print('Entrada Permitida')
        i += 1
        continue

print('Lista de nomes permitidos:',*nome, sep ='\n')
input('Digite qualquer tecla para sair...')
