class Carta:
    naipes_nomes = ["Paus", "Ouros", "Copas", "Espadas"]
    valor_names = [None, "Ás", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Valete", "Dama", "Rei"]

    def __init__(self, naipe=0, valor=2):
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        return '%s de %s' % (Carta.valor_names[self.valor],
                             Carta.naipes_nomes[self.naipe])

    def __eq__(self, other):
        return self.naipe == other.naipe and self.valor == other.valor

    def __lt__(self, other):
        t1 = self.naipe, self.valor
        t2 = other.naipe, other.valor
        return t1 < t2
