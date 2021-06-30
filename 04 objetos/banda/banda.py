from musicos import *
from random import choice

class Banda:
    def __init__(self, instrumentos):
        self.musicos = []
        self.instrumentos = instrumentos

    def presentar(self):
        for m in self.musicos:
            m.presentar()

    def afinar(self):
        for m in self.musicos:
            m.afinar_instrumento()

    def tocar(self):
        for m in self.musicos:
            m.tocar_instrumento()

    def armar_banda(self, nombres):
        for n in nombres:
            self.musicos.append(Musico(n, self.entregar_instrumento()))

    def entregar_instrumento(self):
        return choice(self.instrumentos)
        
if __name__ == '__main__':

    b = Banda([Guitarra(),Bajo(),Tiple()])
    b.armar_banda(["Alejandro", "Juan", "Maria", "Ana"])
    b.presentar()
    b.afinar()
    b.tocar()
