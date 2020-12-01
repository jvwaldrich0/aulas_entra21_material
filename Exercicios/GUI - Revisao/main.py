from tkinter import *
from Packages import Exercicio1 as e

# Root
Base = Tk(className='Revisao')
# Label
Label(Base, text='Joao Vitor Waldrich',
      padx=201,
      pady=50,
      bg='cyan',
      fg='black').grid(row=0, column=0)
# Buttons
Atividade1 = Button(Base, text='Exercicio de Nota Fiscal',
                    padx=187, pady=40,
                    command=lambda: e.exercicio1(Tk(className=' Ativadade 1')),
                    bg='black', fg='white').grid(row=1, column=0)
Atividade2 = Button(Base, text='Exercicio de Loja de tintas',
                    padx=180, pady=40,
                    command=lambda: e.exercicio2(Tk(className=' Ativadade 2')),
                    bg='black', fg='white').grid(row=2, column=0)
Atividade3 = Button(Base, text='Exercicio dos Triangulos',
                    padx=186, pady=40,
                    command=lambda: e.exercicio3(Tk(className=' Ativadade 3')),
                    bg='black', fg='white').grid(row=3, column=0)
Base.mainloop()
