def t():
    return '-' * 10


def cabecalho(empresa):
    return t() + f' Menu {empresa} ' + t()


print(cabecalho(input('Digite o nome da empresa: ')))
