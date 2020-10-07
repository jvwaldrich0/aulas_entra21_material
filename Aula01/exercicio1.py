while True:
    try:
        nome = input('Nome: ').upper()
        sobrenome = input('Sobrenome: ').upper()
        while True:
            cpf = input('CPF(apenas numeros): ')
            if len(cpf) == 11:
                break
        while True:
            rg = input('RG(apenas numeros): ')
            if len(rg) == 7:
                break
        salario = float(input('Salario: R$'))
    except ValueError:
        pass
    else:
        print(f'''
Nome: {nome}
Sobrenome: {sobrenome}
CPF: {cpf[:3]+'.'+cpf[3:6]+'.'+cpf[6:9]+'.'+cpf[9:11]}
RG: {rg[:1]+'.'+rg[1:4]+'.'+rg[4:7]}
Salario: R${salario:.2f}''')