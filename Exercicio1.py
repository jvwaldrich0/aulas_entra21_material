while True:
    escolha = int(input('''
Digite o número relacionado ao respectivo intrumento que você deseja escolher:
1 - Guitarra
2 - Pandeiro
3 - Violão
4 - Bateria
    
Resultado : '''))
    if escolha == 1:
        print('Você escolheu: Guitarra')
    elif escolha == 2:
        print('Você escolheu: Pandeiro')
    elif escolha == 3:
        print('Você escolheu: Violão')
    elif escolha == 4:
        print('Você escolheu: Bateria')
    else:
        print('Digite um número dentro do espectro pré-definido')
    novamente = int(input('''
Deseja executar este código novamente?
1                   - Sim
Qualquer número     - Não

Escolha: '''))
    if novamente == 1:
        continue
    else:
        break
