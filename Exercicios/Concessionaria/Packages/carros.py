from clientes import Pessoa
import sqlite3


class Veiculo:
    """
    Esta classe eh utilizada para os veiculos
    """

    def __init__(self, marca, modelo, cor, proprietario, assentos=None):
        if assentos is None:
            assentos = ['_']
        veiculos = sqlite3.connect('veiculos.db')
        sql = veiculos.cursor()

 #        sql.execute(f'''
 # INSERT INTO carro(cor, marca, modelo, propriedade, assentos)
 # VALUES ({cor}, {marca}, {modelo}, {proprietario}, {assentos});
 # ''')
        valoresSQL = {
            'cor' : cor,
            'marca' : marca,
            'modelo' : modelo,
            'propriedade' : proprietario,
            'assentos' : assentos
        }
        nomes = ['cor', 'marca', 'modelo', 'proprietario', 'assentos']
        for i in nomes:
            sql.execute(f'''
            INSERT INTO carro({i}) VALUES {valoresSQL[i]};''')

        self.marca = valoresSQL['marca']
        self.modelo = valoresSQL['modelo']
        self.cor = valoresSQL['cor']
        self.propriedade = valoresSQL['proprietario']
        self.assentos = int(valoresSQL['assentos'])

        veiculos.commit()

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
    print(carro.cor)
    # for x in range(len(carro.assentos)):
    #     carro.add_passageiro(str(Pessoa(
    #         nome=input(f'Este será o/a {"motorista" if x == 0 else "passageiro(a)"}'
    #                    f'\n\nDigite o nome: '),
    #         cpf=input('Digite o CPF(11 caracteres): '),
    #         dia=int(input('Info do seu nascimento: \nDia = ')),
    #         mes=int(input('Mes = ')),
    #         ano=int(input('Ano = ')),
    #         motorista=True if x == 0 else False,
    #         habilitacao=True if x == 0 else False
    #     )), x)
    # else:
    #     print(*carro.assentos, sep='\n')
