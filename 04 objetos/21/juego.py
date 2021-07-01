from cartas import *

class Juego:

    def __init__(self):
        self.mazo = Mazo()
        self.jugador1 = Mazo(True)
        self.jugador2 = Mazo(True)

    def iniciar_juego(self):
        for i in range(2):
            self.jugador1.agregar_carta(self.mazo.entregar_carta())
            self.jugador2.agregar_carta(self.mazo.entregar_carta())

    def mostrar_juego(self, finalizado = False):
        print("Cartas del jugador 1")
        self.jugador1.mostrar_cartas(finalizado)
        print("Cartas del jugador 2")
        self.jugador2.mostrar_cartas(finalizado)

        valor1 = self.jugador1.valor_mazo()
        valor2 = self.jugador2.valor_mazo()

        print("Jugador 1 = %d y Jugador 2 = %d" %(valor1, valor2))

    def valorar_juego(self):
        valor1 = self.jugador1.valor_mazo()
        valor2 = self.jugador2.valor_mazo()

        if valor1 > valor2 and valor1 <= 21:
            print("Gana el jugador 1")
        elif valor2 > valor1 and valor2 <= 21:
            print("Gana el jugador 2")
        elif valor1 < valor2 and valor2 > 21:
            print("Gana el jugador 1")
        elif valor2 < valor1 and valor1 > 21:
            print("Gana el jugador 2")
        else:
            print("Empate")

    def jugar(self):
        jugando = True
        self.iniciar_juego()

        while jugando:
            self.mostrar_juego()
            if self.jugador1.valor_mazo() < 18:
                self.jugador1.agregar_carta(self.mazo.entregar_carta())
            if self.jugador2.valor_mazo() < 18:
                self.jugador2.agregar_carta(self.mazo.entregar_carta())
            if self.jugador1.valor_mazo() > 21:
                jugando = False
                break
            if self.jugador2.valor_mazo() > 21:
                jugando = False
                break
            if self.jugador1.valor_mazo() >= 18 and self.jugador2.valor_mazo() >= 18:
                jugando = False
                break

        self.mostrar_juego(True)
        self.valorar_juego()

if __name__ == '__main__':
    j = Juego()
    j.jugar()
