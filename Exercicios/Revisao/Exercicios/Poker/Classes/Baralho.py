import random
from .Carta import Carta


class Baralho:
    def __init__(self):
        self.cartas = []
        for naipe in range(4):
            for valor in range(1, 14):
                carta = Carta(naipe, valor)
                self.cartas.append(carta)

    def __str__(self):
        res = []
        for carta in self.cartas:
            res.append(str(carta))
        return '\n'.join(res)

    def addCarta(self, carta):
        self.cartas.append(carta)

    def popCarta(self, i=-1):
        return self.cartas.pop(i)

    def shuffle(self):
        random.shuffle(self.cartas)

    def sort(self):
        self.cartas.sort()

    def moveCartas(self, mao, num):
        for i in range(num):
            mao.addCarta(self.popCarta())
