class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Veiculo:

    def __init__(self, marca, combustivel, max_passageiros, 
        ambiente, num_rodas, economico, cor, autonomia):
        self.marca = marca
        self.combustivel = combustivel
        self.max_passageiros = max_passageiros
        self.ambiente = ambiente
        self.num_rodas = num_rodas
        self.economico = economico
        self.cor = cor
        self.automia = autonomia
        self.passageiros = []

    def adicionar_passageiro(self, pessoa:Pessoa):
        if len(self.passageiros) < self.max_passageiros:
            self.passageiros.append(pessoa)
        else:
            return "não cabe mais ngm!"
        
    def remover_passageiro(self, pessoa:Pessoa):
        pass

    def get_passageiros(self)->list:
        return self.passageiros

class Bike(Veiculo):
    def __init__(self,cor):
        self.__quadro = "18'"

        super().__init__("Caloi", None, 1, "Terra", 
        2, True, cor, None)

    @property
    def quadro(self):
        return self.__quadro

if __name__ == "__main__":
    p = Pessoa("Bruno", 29, "022.121.434-33")
    p2 = Pessoa("Yago", 22, "020.121.434-33")

    v = Veiculo("Volksvagem", "Gasolina", 5, "Terra", 4, True, "Azul", "100km")
    b = Bike("Aluminio")

    b.adicionar_passageiro(p)
    print(b.adicionar_passageiro(p2))

    print(b.passageiros)


