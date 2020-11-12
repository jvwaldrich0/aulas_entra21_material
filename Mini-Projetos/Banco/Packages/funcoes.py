def verificacao(cliente):
    if cliente.conta:
        return 'Já possui conta'
    else:
        return 'Crie uma conta'


def traco(tamanho: int):
    return '-'*tamanho


def listar(cliente):
    for i in range(len(cliente)):
        print(f'{i} - ' + str(cliente[i]))