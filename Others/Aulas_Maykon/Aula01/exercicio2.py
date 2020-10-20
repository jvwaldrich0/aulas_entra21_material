def print_cpf(cpf2):
    return f"{cpf2[:3] + '.' + cpf2[3:6] + '.' + cpf2[6:9] + '.' + cpf2[9:11]}"


def print_rg(rg2):
    return f"{rg2[:1] + '.' + rg2[1:4] + '.' + rg2[4:7]}"


funcionarios = []
while True:
    try:
        escolha = int(input('''
---------- Menu ----------
{0} - Cadastrar funcionário\n{1} - Listar funcionários\n{2} - Editar funcionário\n{3} - Deletar funcionário\n{4} - Sair
> '''.format(1, 2, 3, 4, 5)))

    except ValueError:
        pass
    else:

        # ---- Opcao 1 - Cadastrar ---- #
        if escolha == 1:
            # -- Recolher variaveis -- #
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
            # -- add/rm da lista -- #
            while True:
                print(f'Usuario a ser cadastrado:\nNome: {nome}\nSobrenome: {sobrenome}\nCPF: {print_cpf(cpf)}\nRG: {print_rg(rg)}')
                escolha1 = input('Confirmar(y/n)?\n> ').upper()
                if escolha1 == 'Y':
                    funcionarios += [{'Nome': nome, 'Sobrenome': sobrenome, 'CPF': print_cpf(cpf), 'RG': print_rg(rg)}]
                elif escolha1 == 'N':
                    del nome, sobrenome, cpf, rg
                else:
                    continue
                break

        # ---- Opcao 2 - Listar ---- #
        elif escolha == 2:
            for i in range(len(funcionarios)):
                print('-------------')
                for chaves, valores in funcionarios[i].items():
                    print(chaves, ':', valores)
                print('-------------')
            if len(funcionarios) == 0:
                print('\nCadastre um funcionario\n')

        # ---- Opcao 3 - Editar ---- #
        elif escolha == 3:
            while True:
                try:
                    print('Digite exatamente parametro deseja editar:')
                    for chaves in funcionarios[0]:
                        print(chaves)
                    parametro = input('\n> ')
                    for i in range(len(funcionarios)):
                        for chaves in funcionarios[i]:
                            if parametro == chaves:
                                if parametro == 'CPF':
                                    funcionarios[i][chaves] = print_cpf(input((parametro + '= ')))
                                elif parametro == 'RG':
                                    funcionarios[i][chaves] = print_rg(input((parametro + '= ')))
                                else:
                                    funcionarios[i][chaves] = input(parametro + '= ').upper()
                    else:
                        del parametro
                        break
                except IndexError:
                    print('\nCadastre no minimo um usuario\n')
                    break

        # ---- Opcao 4 - Deletar ---- #
        elif escolha == 4:
            print('Digite o nome do funcionario que deseja substituir: ')
            for i in range(len(funcionarios)):
                print(funcionarios[i]['Nome'])
            parametro = input('\n> ').upper()
            for i in range(len(funcionarios)):
                if funcionarios[i]['Nome'] == parametro:
                    del funcionarios[i]

        # ---- Opcao 5 - Sair ---- #
        elif escolha == 5:
            break