#!/bin/python3
import random
from itertools import permutations
from os import system, name
import unicodedata


def clear():
    """Limpeza da tela
    > Argumentos:
        - Sem argumentos.

    > Output:
        - Sem output.
    """
    # Limpa terminal antes de cada execução
    # "cls" para windows e "clear" para linux/mac (posix)
    system('cls') if name == 'nt' else system('clear')


def exercicio1():
    """
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
11 + 8 + 5 = 100 - 24 = 76%
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
    """
    while True:
        try:
            valor_hora = float(input('Quanto voce ganhar por hora?\n> '))
            hora_trabalho = int(input('Quantas horas voce trabalhou?\n> '))
        except ValueError:
            print('\nDigite um numero!\n')
        except:
            print('\nDeu problema!\n')
        else:
            salario_bruto = valor_hora * hora_trabalho
            print(f'''
---------------------------------------
            Nota Fiscal
---------------------------------------
Salário Bruto           R${salario_bruto:.2f}
    - IR (11%)          R${(salario_bruto * 0.11):.2f}
    - INSS (8%)         R${(salario_bruto * 0.8):.2f}
    - Sindicato ( 5%)   R${salario_bruto * 0.5:.2f}
---------------------------------------
Salário Liquido : R${(salario_bruto * 0.76):.2f}
''')
            break


######################################################################################################

def exercicio2():
    """
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
    pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
    latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar
    apenas latas de 18 litros; comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o
    desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    considere latas cheias.
    """
    repetir = True
    while True:
        try:
            while True:
                largura = float(input('Largura da parede:'))
                altura = float(input('Altura da parede:'))
                if largura and altura > 0:
                    break
                else:
                    print('Numero negativo detectado')
            area = largura * altura
            litros_necessarios = float(area / 6) * 1.1
            if litros_necessarios < 1:
                litros_necessarios = 1
            print(f'---- Info da parede ----',
                  f"\nDimensão: {largura:.0f}x{altura:.0f}\nArea: {area} m²",
                  f"\nQuantia necessaria: {litros_necessarios:.2f}L de latas tinta"
                  if int(litros_necessarios) != 1
                  else f"\nQuantia necessaria: {int(litros_necessarios)}L de lata tinta")
            escolha = int(input('''O que voce deseja fazer?
1 - Comprar apenas latas de 18 litros
2 - Comprar apenas galões de 3,6 litros
3 - Misturar latas e galões
> '''))
            total = 0
            galoes = 0
            latas = 0
            while True:
                if (litros_necessarios >= 18) and (escolha != 2):
                    litros_necessarios -= 18
                    total += 80
                    latas += 1
                elif (litros_necessarios > 0) and (escolha != 1):
                    litros_necessarios -= 3.6
                    total += 25
                    galoes += 1
                elif litros_necessarios <= 0:
                    break
                else:
                    total += 80
                    latas += 1
                    break
        except ValueError:
            print('Digite apenas numeros')
        except:
            pass
        else:
            while True:
                print(f'{latas} Latas' if latas > 1 else f'{latas} Lata',
                      f'{galoes} Galoes' if galoes > 1 else f'{galoes} Galao', sep='\n&&\n')
                repetir = True if input("Digite 'r' para repetir: ").upper() == 'R' else False
                break
        finally:
            if not repetir:
                break


#######################################################################################################


def exercicio3():
    """
    Faça um Programa que peça os 3 lados de um triângulo.
    O programa deverá informar se os valores podem ser um triângulo.
    Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    """
    repetir = True
    while True:
        try:
            x, y, z = [int(var) for var in [input(
                f"{'Por favor informe o os lados de um triangulo:' if i == 'x' else ''} "
                f"\n{i}: ") for i in ['x', 'y', 'z']]]
        except ValueError:
            print('\nApenas numeros por favor!\n')
        else:
            if (x == y) and (y == z):
                print('\nTRIANGULO EQUILATERO! TODOS OS LADOS SAO IGUAIS!\n')
            elif x == y or x == z:
                print(f'\nTRIANGULO ISOCELES! x = {"y" if x == y else "z"}\n')
            else:
                print('\nTRIANGULO ESCALENO!\n')
            repetir = True if input("Digite 'r' para repetir: ").upper() == 'R' else False
            break
        finally:
            if not repetir:
                break


#######################################################################################################

def exercicio4():
    """
    Faça um programa que gera uma lista dos números primos existentes entre 1 e
    um número inteiro informado pelo usuário.
    """

    def primo(n):
        for val in range(2, n):
            if n % val == 0:
                return False
        return True

    print(*[val for val in range(2, int(input('Exibir primos até o número: ')) + 1) if primo(val)], sep=' - ')


#######################################################################################################
def exercicio5():
    """
    Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor .
    Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para
    Gerar numeros aleatórios, simulando os lançamentos dos dados.
    """
    resultado = [[random.randint(1, 6) for i in range(100)], [random.randint(1, 6) for i in range(100)]]
    acerto = len([i for i in range(100) if resultado[0][i] == resultado[1][i]])
    print(resultado[0], resultado[1], f'{acerto} acertos', sep='\n')


#######################################################################################################
def exercicio6():
    """
    # Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual
    # a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1
    # a 9:

    #     8  3  4
    #     1  5  9
    #     6  7  2

    Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
    Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
    Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
    """

    print(f"\n{'*' * 5} QUADRADOS MÁGICOS DE ORDEM 3x3 {'*' * 5}\n")
    quadrados = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    for quadrados in quadrados:
        soma = quadrados[0] + quadrados[1] + quadrados[2]
        valid = True

        # soma das linhas
        for i in range(0, 7, 3):
            if (quadrados[i] + quadrados[i + 1] + quadrados[i + 2]) != soma:
                valid = False

        # soma das colunas
        for i in range(0, 3):
            if (quadrados[i] + quadrados[i + 3] + quadrados[i + 6]) != soma:
                valid = False

        # soma das diagonais
        s = (quadrados[0] + quadrados[4] + quadrados[8])
        ss = (quadrados[2] + quadrados[4] + quadrados[6])
        if s != soma or ss != soma:
            valid = False

        if valid:
            print('[', end=" ")
            for i in range(0, 7, 3):
                print(f"[{quadrados[i]} {quadrados[i + 1]} {quadrados[i + 2]}]", end=" ")
            print(']')


#######################################################################################################

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u.
def exercicio7():
    def countChar(char: str, phrase: str) -> int:
        new_ph = unicodedata.normalize("NFD", phrase).upper()
        count = new_ph.count(char.upper())

        return count

    print(f"{'*' * 10}  CONTADOR DE ESPAÇOS EM BRANCO E VOGAIS  {'*' * 10}\n")
    frase = input("Informe uma frase: ")

    print(f"""
        FRASE: {frase}
        NÚMERO DE ESPAÇOS EM BRANCO: {countChar(' ', frase)}
        NÚMERO DE VOGAIS: 
        A: {countChar('a', frase)}
        E: {countChar('e', frase)}
        I: {countChar('i', frase)}
        O: {countChar('o', frase)}
        U: {countChar('u', frase)}
        """)

########################################################################################################

# construa um analisador das 5 principais combinações de mãos do poker.
# Para isso utilize como base as classes descritas em:
# https://penseallen.github.io/PensePython2e/18-heranca.html
# considere como regra o poker fechado, em que a mão do jogador, já tem a combinação de 5 cartas :)
