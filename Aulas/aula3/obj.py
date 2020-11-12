class Relogio:
    def __init__(self, ponteiro, marca, material, cor,
        paraguaio, valor):
        self.ponteiro = ponteiro
        self.paraguaio = paraguaio

    def __str__(self):
        pass

    def som(self):
        if not self.paraguaio:
            return "tick tok"
        else:
            return "..."

    def mostrar_horas(self):
        print("hora é :" )

