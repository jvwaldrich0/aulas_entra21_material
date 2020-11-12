from veiculos import Pessoa

class Banco():
    def __init__(self):
        pass

class DataSaver():
    def __init__(self):
        pass
    
    @staticmethod
    def savePessoa(pessoa:Pessoa):
        p = Pessoa("Bruno", 29, "022.121.434-33")
        return p


class Conta():
    def __init__(self, banco:Banco, pessoa: Pessoa):
        pass


if __name__ == "__main__":
    while True:
        valor = int(input(
            """Digite a operação desejada
            1 - Cadastrar Pessoa
            2 - Cadastrar Conta
            3 - Visualizar Saldo
            4 - Fazer um depósito
            5 - Sair\n"""))

        if(valor == 1):
            print(DataSaver.savePessoa(Pessoa()))

        if(valor == 5):
            print("Agradecemos a sua visita!")
            break
