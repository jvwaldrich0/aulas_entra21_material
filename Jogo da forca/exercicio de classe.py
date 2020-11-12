class plastico:
    def __init__(self, dono, tipo, local):
        self.local = local
        self.dono = dono
        self.tipo = tipo
    def print(self):
        print(self.local, self.dono, self.tipo)

class empresa:
    def __init__(self, dono, local, funcionario):
        self.dono = dono
        self.local = local
        self.funcionario = funcionario
    def print(self):
        print(self.local, self.dono, self.funcionario)

class startup:
    def __init__(self, dono, local, funcionario):
        self.dono = dono
        self.local = local
        self.funcionario = funcionario
    def print(self):
        print(self.local, self.dono, self.funcionario)

class monitor:
    def __init__(self, hz, tamanho, preco):
        self.preco = preco
        self.tamanho = tamanho
        self.hz = hz
    def print(self):
        print(self.hz, self.tamanho, self.preco)

class pc:
    def __init__(self, preco, qualidade, energia):
        self.energia = energia
        self.qualidade = qualidade
        self.preco = preco
    def print(self):
        print(self.energia, self.preco, self.qualidade)