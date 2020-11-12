# Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo;
# por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)

class Veiculo:
    def __init__(self, carro: str, ano: int, marca: str, cor: str, dono: str):
        self.carro = carro
        self.ano = ano
        self.marca = marca
        self.cor = cor
        self.dono = dono
        self.ligado = False

    def __str__(self):
        return f'{self.carro} {self.cor} {self.ano} do {self.dono}'

    def ligar(self):
        if self.ligado:
            return 'Já esta ligado'
        else:
            self.ligado = True
            return 'Ligado'

    def desligar(self):
        if not self.ligado:
            return 'Já está desligado'
        else:
            self.ligado = False
            return 'Desligado'

    @staticmethod
    def freiar():
        return 'freiando...'

    def andar(self):
        if self.ligado:
            return 'Andando'
        else:
            return 'Ligue o carro'


class Corola(Veiculo):
    def __init__(self, ano, cor, dono):
        super().__init__('Corola', ano, 'Toyota', cor, dono)


class Gol(Veiculo):
    def __init__(self, ano, cor, dono):
        super().__init__('Gol Bolinha', ano, 'Volkwagen', cor, dono)


class HotWheels(Veiculo):
    def __init__(self, ano, cor, dono):
        super().__init__('Hot Whilson', ano, 'Ford GT', cor, dono)


if __name__ == '__main__':
    h = HotWheels(
            int(input('Info Hot Whilson\nAno: ')),
            input('Cor: '),
            input('Dono: '))

    g = Gol(
            int(input('Info Gol\nAno: ')),
            input('Cor: '),
            input('Dono: '))

    c = Corola(
            int(input('Info Corola\nAno: ')),
            input('Cor: '),
            input('Dono: '))

    print(
        f'{h}',
        f'{g}',
        f'{c}',
        sep='\n')
