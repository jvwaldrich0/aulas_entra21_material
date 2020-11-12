# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

from datetime import date
#função para calcular idade
def idade():
    # Input do dia do nascimento
    print('Informe sua data de nascimento:')
    sday = int(input('Dia: '))
    smonth = int(input('Mês: '))
    syear = int(input('Ano: '))
    start_date = date(syear, smonth, sday)
    year = int(start_date.year)
    month = int(start_date.month)
    day = int(start_date.day)
    # Pegando valores do dia atual
    final_day = date.today()
    fday = final_day.today().day
    fmonth = final_day.today().month
    fyear = final_day.today().year
    #----- Loop
    while True:
        try:
            if start_date.replace(year=year, month=month, day=day) == final_day.replace(year=fyear, month=fmonth,
                                                                                        day=fday):
                return final_day.year - start_date.year - ((final_day.month, final_day.day) < (start_date.month, start_date.day))
        except ValueError:
            if month == 1 or 3 or 5 or 7 or 8 or 10:
                day = 1
                month += 1
            elif month == 4 or 6 or 9 or 11:
                day = 1
                month += 1
            elif month == 2:
                day = 1
                month += 1
        else:
            day += 1
            if (month >= 12) and (day > 31):
                day = 1
                month = 1
                year += 1

while True:
    try:
        nome = input('Vamos cadastrar um usuário?\nDigite seu nome: ')
        idade = int(idade()) #Chamei a função acima
        endereco = input('Digite seu endereço: ')
        email = input('Digite seu email: ')
        telefone = input('Digite seu telefone: ')
        while True:
            try:
                choice = int(input('1 - Informar os dados\n2 - Informar endereço \n3 - Informar contato\nEscolha: '))
                if choice == 1:
                    print(f'Nome = {nome}\nIdade = {idade}')
                elif choice == 2:
                    print(f'Nome = {nome}\nEndereço = {endereco}')
                elif choice == 3:
                    print(f'Nome = {nome}\nEmail: {email}\nTelefone: {telefone}')
            except ValueError:
                # caso o usuario digite um valor errado
                print('\nVocê digitou um valor errado, tente novamente\n')
            else:
                escolha = int(input('\nDigite 1 para reiniciar: '))
                if escolha != 1:
                    break
    except ValueError:
        #caso o usuario digite um valor errado
        print('\nVocê digitou um valor errado, tente novamente\n')
    else:
        escolha = int(input('\nDigite 1 para recadastrar: '))
        if escolha != 1:
            break
