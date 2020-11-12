from os import system, name


class JogoForca:
    def __init__(self, arquivo):
        with open(arquivo) as arquivos:
            try:
                self.palavra = str(arquivos.readlines()[0])
                self.tamanho_palavra = len(self.palavra) - 1
            except ValueError:
                raise ValueError('Segunda linha não é um número')
        with open(arquivo) as arquivos:
            self.chances = int(arquivos.readlines()[1])
        self.acerto = ['_'] * self.tamanho_palavra

    def __str__(self):
        return f'Palavra = {self.palavra}\nChances = {self.chances}'

    def __repr__(self):
        return 'Classe de para jogo da forca'

    def msg_start(self, tamanho):
        if tamanho == 1:
            print(f'A palavra a ser adivinhada possui {self.tamanho_palavra} letra,'
                  f' você possui {self.chances} para acertar. Boa sorte!\n')
        else:
            print(f'A palavra a ser adivinhada possui {self.tamanho_palavra} letras,'
                  f' você possui {self.chances} para acertar. Boa sorte!\n')

    @staticmethod
    def clear():
        if name == 'nt': # Windows
            return system('cls') or None
        else: # Linux / MacOS
            return system('clear') or None

    def traco(self, letra):
        for i in range(len(self.acerto)):
            for x in self.soletrar(letra):
                if letra == x:
                    self.acerto[i] = letra
        return self.acerto

    def tratamento(self, letra, mesma_letra:list) -> str :
        try:
            float(letra)
        except ValueError:
            if len(letra) != 1:
                raise AttributeError('Apenas uma letra')
            for letras in mesma_letra:
                if letras == letra:
                    raise TypeError('Mesma Letra!')
            else:
                return letra
        else:
            raise ValueError('Não é permitido número')

    def soletrar(self, palavra):
        char = []
        for i in range(len(palavra)):
            if i == len(palavra) - 1:
                pass
            else:
                char += [palavra[i]]
        return char
