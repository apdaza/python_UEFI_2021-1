from random import choice

class Animal:
    def informar_tipo(self):
        print(type(self))

    def comunicar(self):
        pass

class Gato(Animal):
    def comunicar(self):
        print("miau")

class Perro(Animal):
    def comunicar(self):
        print("guau")

class Loro(Animal):
    def comunicar(self):
        print("rua")

class Cacatua(Animal):
    def comunicar(self):
        print("pia-rua")

class Tienda:
    def __init__(self):
        self.animal = None
        self.animales = [Perro(), Loro(), Gato(), Cacatua()]

    def seleccionar_animal(self):
        self.animal = choice(self.animales)
        
if __name__ == '__main__':
    t = Tienda()
    t.seleccionar_animal()
    t.animal.informar_tipo()
    t.animal.comunicar()
