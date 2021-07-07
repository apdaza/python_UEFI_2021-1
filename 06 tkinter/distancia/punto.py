from math import sqrt

class Punto:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def calcular_distancia(self, punto):
        return sqrt(((self.x - punto.x) ** 2) + ((self.y - punto.y) ** 2))

    def informar_propiedades(self):
        print("(%d, %d)" %(self.x, self.y))

if __name__ == '__main__':
    p1 = Punto()
    p2 = Punto(5, 5)

    p1.informar_propiedades()
    p2.informar_propiedades()

    print(p1.calcular_distancia(p2))
