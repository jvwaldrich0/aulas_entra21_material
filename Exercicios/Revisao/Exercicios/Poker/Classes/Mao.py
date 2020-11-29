from .Baralho import Baralho


class Mao(Baralho):
    def __init__(self, label=''):
        self.cartas = []
        self.label = label

    def getValores(self):
        valores = []

        # gerando lista dos valores das cartas
        for carta in self.cartas:
            valores.append(carta.valor)
        return valores


    def getNaipes(self) -> list:
        naipes = []

        # gerando lista dos naipes das cartas
        for carta in self.cartas:
            naipes.append(carta.naipe)
        return naipes


    def countValoresRepetidos(self) -> list:
        valores = self.getValores()

        # removendo elementos repetidos
        valores_norepeat = []
        for valor in valores:
            if not valor in valores_norepeat:
                valores_norepeat.append(valor)

        # gerando lista contadora de valores repetidos
        count = []
        for valor in valores_norepeat:
            contador = valores.count(valor)
            if contador > 1:
                count.append(contador)
        return sorted(count)


    # falta verificar para a sequencia 10, 11, 12, 13, 1
    def sequencia(self):
        valores = self.getValores()
        valores = sorted(valores)

        anterior = valores[0]
        valores.remove(anterior)
        for valor in valores:
            if valor - 1 == anterior:
                anterior = valor
            else:
                return False
        if not self.flush():
            return True


    def flush(self):
        # resgatando lista com todos os naipes
        naipes = self.getNaipes()

        # verificando se todos são iguais
        if naipes.count(naipes[0]) == 5:
            return True

