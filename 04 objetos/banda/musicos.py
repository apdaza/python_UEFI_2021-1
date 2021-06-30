from instrumentos import *
from random import choice

class Musico:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento

    def presentar(self):
        print("mi nombre es %s y toco el instrumento %s"
              %(self.nombre, self.instrumento.presentar()))

    def afinar_instrumento(self):
        self.instrumento.afinar(choice(["Do", "Re", "Mi"]))

    def tocar_instrumento(self):
        self.instrumento.tocar()

if __name__ == '__main__':
    m = Musico("Alejandro", Tiple())
    m.presentar()
    m.afinar_instrumento()
    m.tocar_instrumento()
