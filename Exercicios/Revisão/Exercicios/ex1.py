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


