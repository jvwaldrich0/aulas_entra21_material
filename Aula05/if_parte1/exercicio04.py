# Exercicio 4
# Escreva um programa que peça a nota de um aluno
# 
# Se a nota for 7 ou mais deve aparecer a mensagem: "Aprovado"
# 
# Caso contrário deve aparecer a mensagem: "Reprovado"

print('Software que aprova ou reprova um aluno baseado em suas notas')
while True:
    try:
        nota = int(input('Digite a média da sua nota: '))
        if nota >= 7:
            print('\nAprovado\n')
        else:
            print('\nReprovado\n')
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para : '))
        if escolha != 1:
            break