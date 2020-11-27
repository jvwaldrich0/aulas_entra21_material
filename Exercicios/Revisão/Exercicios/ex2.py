def exercicio2():
    """
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
    pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
    latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar
    apenas latas de 18 litros; comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o
    desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    considere latas cheias.
    """
    repetir = True
    while True:
        try:
            while True:
                largura = float(input('Largura da parede:'))
                altura = float(input('Altura da parede:'))
                if largura and altura > 0:
                    break
                else:
                    print('Numero negativo detectado')
            area = largura * altura
            litros_necessarios = float(area / 6) * 1.1
            if litros_necessarios < 1:
                litros_necessarios = 1
            print(f'---- Info da parede ----',
                  f"\nDimensão: {largura:.0f}x{altura:.0f}\nArea: {area} m²",
                  f"\nQuantia necessaria: {int(litros_necessarios )}L de latas tinta"
                  if int(litros_necessarios) != 1
                  else f"\nQuantia necessaria: {int(litros_necessarios )}L de lata tinta")
            escolha = int(input('''O que voce deseja fazer?
1 - Comprar apenas latas de 18 litros
2 - Comprar apenas galões de 3,6 litros
3 - Misturar latas e galões
> '''))
            total = 0
            galoes = 0
            latas = 0
            while True:
                if (litros_necessarios >= 18) and (escolha != 2):
                    litros_necessarios -= 18
                    total += 80
                    latas += 1
                elif (litros_necessarios > 0) and (escolha != 1):
                    litros_necessarios -= 3.6
                    total += 25
                    galoes += 1
                elif litros_necessarios <= 0:
                    break
                else:
                    total += 80
                    latas += 1
                    break
        except ValueError:
            print('Digite apenas numeros')
        except:
            pass
        else:
            while True:
                print(f'{latas} Latas' if latas > 1 else f'{latas} Lata',
                      f'{galoes} Galoes' if galoes > 1 else f'{galoes} Galao', sep='\n&&\n')
                escolha = int(input(f'\nTotal: R${total:.2f}\n\nPressione 1 para prosseguir: '))
                print('Compra feita com sucesso' if escolha == 1 else 'Compra cancelada')
                rep = input("Digite 'r' para repetir: ").upper()
                repetir = True if rep == 'R' else False
                break
        finally:
            if not repetir:
                break
