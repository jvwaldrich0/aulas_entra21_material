def leitura():
    while True:
        try:
            n1 = int(input(f'Digite numero 1: '))
            n2 = int(input(f'Digite numero 2: '))
            break
        except ValueError:
            print('Digitou algo errado, tenta de novo')
    div = n1 / n2
    return f'\n{n1} / {n2} = {div}'


print(leitura())
