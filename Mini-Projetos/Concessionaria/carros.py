from clientes import Pessoa


class Veiculo:
    def __init__(self, marca, modelo, cor, proprietario, assentos=['_']):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.propriedade = proprietario
        self.assentos = assentos

    def add_passageiro(self, passageiro, i):
        self.assentos[i] = passageiro


class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, proprietario, assentos=['_'] * 2):
        super().__init__(marca, modelo, cor, proprietario, assentos)


class Carro(Veiculo):

    def __init__(self, marca, modelo, cor, proprietario, assentos=['_'] * 5):
        super().__init__(marca, modelo, cor, proprietario, assentos)


if __name__ == '__main__':
    carro = Carro('Toyota', 'Lamborguini', 'Laranja', 'Seu Zé')
    for x in range(len(carro.assentos)):
        carro.add_passageiro(str(Pessoa(
            nome=input(f'Este será o/a {"motorista" if x == 0 else "passageiro(a)"}'
                       f'\n\nDigite o nome: '),
            cpf=input('Digite o CPF(11 caracteres): '),
            dia=int(input('Info do seu nascimento: \nDia = ')),
            mes=int(input('Mes = ')),
            ano=int(input('Ano = ')),
            motorista = True if x == 0 else False,
            habilitacao = True if x == 0 else False
        )), x)
    else:
        print(*carro.assentos, sep='\n')
