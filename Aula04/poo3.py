#parent and child classes
class Animal:
    def __init__(self, habitat, classe):
        self.habitat = habitat
        self.classe = classe

    def som(self):
        return "???"

class Cachorro(Animal):
    def __init__(self, habitat):
        super().__init__(habitat, "Mamifero")

    def som(self):
        return "AU AU"

class Lagarto(Animal):
    def __init__(self, habitat):
        super().__init__(habitat, "Réptil")

    # def som(self):
    #     return "???"

class Pato(Animal):
    def __init__(self, habitat):
        self.__atributo_secreto = "O pato tem quantas patas?"
        super().__init__(habitat, "Ave")

    def som(self):
        return "Quack"
    
    def contar_segredo(self):
        return self.__atributo_secreto


#encapsulamento
pato = Pato("Lagoa")
print(pato.som())
print(pato.contar_segredo())

#polimorfismo
cachorro = Cachorro("Doméstico")
lagarto = Lagarto("Floresta")

zoologico = [pato, cachorro, lagarto]

for animal in zoologico:
    print(f"O {type(animal).__name__} faz {animal.som()}")
