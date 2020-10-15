def leitura_ex3():
    n = []
    for i in range(3):
        while True:
            try:
                n += [float(input(f'Digite o numero {i}: '))]
                break
            except ValueError:
                print('Tenta de novo')
    else:
        media = (n[0] + n[1] + n[2]) / 3
        return f'{n[0]} + {n[1]} + {n[2]} / 3 = {media}'


print(leitura_ex3())
