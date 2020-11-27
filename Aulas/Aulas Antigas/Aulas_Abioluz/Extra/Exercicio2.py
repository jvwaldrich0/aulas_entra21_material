while True:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('\nDigite o segundo número: '))

    #soma
    print(f'''
Resultado das operações matemáticas básicas:

Soma:           {numero1} + {numero2} = {numero1 + numero2}
 
Subtração:      {numero1} - {numero2} = {numero1 - numero2}
                {numero2} - {numero1} = {numero2 - numero1}

Multiplicação:  {numero1} * {numero2} = {numero1*numero2}
    
Divisão:        {numero1} / {numero2} = {numero1/numero2}
                {numero2} / {numero1} = {numero2/numero1}
''')
    novamente = int(input('''
Deseja executar este código novamente?
1                   - Sim
Qualquer número     - Não

Escolha: '''))
    if novamente == 1:
        continue
    else:
        break