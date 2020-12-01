from tkinter import *
import os


def exercicio1(base_tkinter):
    def gerar_notafiscal(base):
        try:
            a = int(valor_hora.get())
            b = int(hora_trabalho.get())
            salario_bruto = a * b
            with open('Data/notafiscal.txt', 'w') as file:
                file.write(
                    f'''
------------------------------------------------------------------ Nota Fiscal ----------------------------------------
+ Salário Bruto:    R${salario_bruto:.2f}
-----------------------------------------------------------------------------------------------------------------------
- IR (11%):          R${(salario_bruto * 0.11):.2f}
- INSS (8%):         R${(salario_bruto * 0.08):.2f}
- Sindicato (5%):    R${salario_bruto * 0.05:.2f}
-----------------------------------------------------------------------------------------------------------------------
= Salário Liquido : R${(salario_bruto * 0.76):.2f}
''')
            test = Label(base, text=f'Nota fiscal salva: {os.path.join(os.getcwd(), "Data/notafiscal.txt")}')
            test.grid(row=4, column=1)
        except ValueError:
            a = Label(base, text='Digite um numero inteiro!', padx=50, pady=50)
            a.grid(row=4, column=1)
        else:
            # ----- Ler Nota Fiscal --------
            ler_nota = Button(base_tkinter, text='Ler Nota Fiscal',
                              command=lambda: ler_notafiscal())
            ler_nota.grid(row=3, column=1)

    def ler_notafiscal():
        with open('Data/notafiscal.txt') as file:
            test1 = Label(Tk(className='Nota Fiscal'), text=file.read())
            test1.grid(row=0, column=0)

    # -------- Valor Hora ----------
    # Label
    Label(base_tkinter, text='Quanto voce ganha por hora? R$').grid(row=1, column=0)
    # Entrada
    valor_hora = Entry(base_tkinter, width=50)
    valor_hora.grid(row=1, column=1)
    # ------ Hora Trabalho ---------
    # Label
    Label(base_tkinter, text='Quanto horas voce trabalhou? R$').grid(row=2, column=0)
    # Entrada
    hora_trabalho = Entry(base_tkinter, width=50)
    hora_trabalho.grid(row=2, column=1)
    # ----- Gerar Nota Fiscal ------
    gerar_nota = Button(base_tkinter, text='Gerar Nota Fiscal',
                        command=lambda: gerar_notafiscal(base_tkinter))
    gerar_nota.grid(row=3, column=0)


def exercicio2(base_tkinter):
    def verificar_valores(base):
        largura = int(largura_parede.get())
        altura = int(altura_parede.get())
        if int(largura_parede.get()) > 0 and int(largura_parede.get()) > 0:
            info_compra(base, largura, altura)
        else:
            Label(base_tkinter, text='Numero negativo detectado!').grid(row=2, column=1)

    def resultado(base, total, galoes, latas):
        Label(base, text=f'Latas' if latas > 1 else f'Lata').grid(row=0, column=0)
        Label(base, text=f'{latas}').grid(row=0, column=1)
        Label(base, text=f'Galoes' if galoes > 1 else f'Galao').grid(row=1, column=0)
        Label(base, text=f'{galoes}').grid(row=1, column=1)
        Label(base, text=f'Total: ').grid(row=3, column=0)
        Label(base, text=f'R${float(total):.2f}').grid(row=3, column=1)

    def calculo(litros_necessarios, escolha: int):
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
        resultado(Tk(className='Resultado'), total, galoes, latas)

    def info_compra(base, largura, altura):
        area = largura * altura
        litros_necessarios = float(area / 6) * 1.1
        if litros_necessarios < 1:
            litros_necessarios = 1
        # Titulo
        Label(base, text='Info Parede').grid(row=0, column=1)
        # Left
        Label(base, text='Dimensao: ').grid(row=1, column=0)
        Label(base, text='Quantia Necessaria: ').grid(row=2, column=0)
        Label(base, text='Area: ').grid(row=3, column=0)
        # Right
        Label(base,
              text=f"{largura}x{altura}").grid(row=1, column=2)
        Label(base,
              text=f"{litros_necessarios:.2f}L de latas tinta").grid(row=2, column=2)
        Label(base,
              text=f'{area} m²').grid(row=3, column=2)
        # Centro
        Label(base, text='O que voce deseja fazer?').grid(row=4, column=1)
        # Entry
        Button(base, text='Comprar apenas latas de 18 litros',
               bg='cyan', fg='black',
               command=lambda: calculo(litros_necessarios, 1)).grid(row=5, column=1)
        Button(base, text='Comprar apenas galões de 3,6 litros',
               bg='cyan', fg='black',
               command=lambda: calculo(litros_necessarios, 2)).grid(row=6, column=1)
        Button(base, text='Misturar latas e galões',
               bg='cyan', fg='black',
               command=lambda: calculo(litros_necessarios, 3)).grid(row=7, column=1)

    # ------ Largura Entry ------
    # Label Left
    Label(base_tkinter, text='Largura da parede ').grid(row=0, column=0)
    # Entry
    largura_parede = Entry(base_tkinter, width=10, justify='right')
    largura_parede.grid(row=0, column=1)
    # Label Right
    Label(base_tkinter, text='m').grid(row=0, column=2)
    # ------ Altura Entry ------
    # Label Left
    Label(base_tkinter, text='Altura da parede ').grid(row=1, column=0)
    # Entry
    altura_parede = Entry(base_tkinter, width=10, justify='right')
    altura_parede.grid(row=1, column=1)
    # Label Right
    Label(base_tkinter, text='m').grid(row=1, column=2)
    # Botao
    Button(base_tkinter, text='Verificar',
           command=lambda: verificar_valores(Tk(className='Compra'))).grid(row=2, column=0)


def exercicio3(base_tkinter):
    def resultado(base, x, y, z):
        if x == y and y == z:
            a = Label(base, text='TRIANGULO EQUILATERO! TODOS OS LADOS SAO IGUAIS!')
            a.grid(row=5, column=1)
        elif x == y or x == z or y == z:
            a = Label(base, text=f'\nTRIANGULO ISOCELES! {"x" if x == y or x == z else "y"} = {"y" if x == y else "z"}\n')
            a.grid(row=5, column=1)
        else:
            a = Label(base, text='\nTRIANGULO ESCALENO!\n')
            a.grid(row=5, column=1)
        a.after(3500, lambda: a.destroy())

    # Warning
    Label(base_tkinter, text='Por favor informe o os lados de um triangulo').grid(row=0, column=1)
    # x
    Label(base_tkinter, text='x').grid(row=1, column=0)
    x = Entry(base_tkinter, width=10)
    x.grid(row=1, column=2)

    # y
    Label(base_tkinter, text='y').grid(row=2, column=0)
    y = Entry(base_tkinter, width=10)
    y.grid(row=2, column=2)

    # z
    Label(base_tkinter, text='z').grid(row=3, column=0)
    z = Entry(base_tkinter, width=10)
    z.grid(row=3, column=2)

    b = Button(base_tkinter,
               text='Check',
               bg='red',
               fg='black',
               command=lambda: resultado(base_tkinter,
                                         int(x.get()),
                                         int(y.get()),
                                         int(z.get())
                                         )).grid(row=4,
                                                 column=1)
    b.after(1000, lambda: b.destroy())



