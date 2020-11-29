from .Classes.Baralho import Baralho
from .Classes.Carta import Carta
from .Classes.Mao import Mao


def geraMao() -> object:
    baralho = Baralho()
    baralho.shuffle()
    mao = Mao()
    baralho.moveCartas(mao, 5)
    mao.sort()
    return mao


def verifica_combinacao(mao: object) -> str:
    repetidos = mao.countValoresRepetidos()
    combinacao = ''

    if repetidos.count(2) == 1 and not repetidos.count(3):
        combinacao = ' UM PAR'
    elif repetidos.count(2) == 2:
        combinacao = 'DOIS PARES'
    elif repetidos.count(3) and not repetidos.count(2):
        combinacao = 'TRINCA'
    elif repetidos.count(4):
        combinacao = 'QUADRA'
    elif repetidos.count(3) and repetidos.count(2):
        combinacao = 'FULL HOUSE'
    elif mao.sequencia():
        combinacao = 'SEQUÊNCIA'
    elif mao.flush():
        combinacao = 'FLUSH'
    elif mao.flush() and mao.sequencia():
        combinacao = 'STRAIGHT FLUSH'
    else:
        combinacao = 'nada de interessante. Tente novamente.'

    return combinacao


def main():
    print(f"{'*' * 8} ANALISADOR DE COMBINAÇÃO DAS MÃOS DO POKER {'*' * 8}\n\n", "Embaralhando as cartas...",
          "Dando as cartas...",
          f"{'*' * 5} SUAS CARTAS NESSA RODADA {'*' * 5}", sep='\n')
    mao = geraMao()
    print(mao)
    print(f"Você pegou {verifica_combinacao(mao)}\n")
