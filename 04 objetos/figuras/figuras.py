from punto import *
from math import pi

class Figura:

    def __init__(self, p1, p2):
        self.punto1 = p1
        self.punto2 = p2
        self.area = 0
        self.perimetro = 0

    def informar_propiedades(self):
        self.calcular_area()
        self.calcular_perimetro()
        print("tipo figura: %s" % str(type(self)).split(".")[1][:-2])
        print("el area es: %d" % self.area)
        print("el perimetro es: %d" % self.perimetro)

class Circulo(Figura):

    def calcular_area(self):
        radio = self.punto1.calcular_distancia(self.punto2)
        self.area = pi * radio ** 2

    def calcular_perimetro(self):
        radio = self.punto1.calcular_distancia(self.punto2)
        self.perimetro = 2 * pi * radio

class Rectangulo(Figura):
    
    def calcular_area(self):
        temporal = Punto(self.punto1.x, self.punto2.y)
        base = self.punto1.calcular_distancia(temporal)
        altura = self.punto2.calcular_distancia(temporal)
        self.area = base * altura

    def calcular_perimetro(self):
        temporal = Punto(self.punto1.x, self.punto2.y)
        base = self.punto1.calcular_distancia(temporal)
        altura = self.punto2.calcular_distancia(temporal)
        self.perimetro = 2 * (base + altura)

if __name__ == '__main__':
    f = Rectangulo(Punto(), Punto(5, 5))
    f.informar_propiedades()
