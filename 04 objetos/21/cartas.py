from random import shuffle

class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def valor_carta(self):
        if self.valor in ["J", "Q", "K"]:
            return 10
        elif self.valor == "A":
            return 1
        else:
            return int(self.valor)

    def mostrar_carta(self):
        print("%s de %s" %(self.valor, self.pinta))

class Mazo:
    def __init__(self, jugador = False):
        if jugador:
            self.cartas = []
        else:
            self.cartas = [Carta(v, p)
                           for v in ['A', 'J', 'Q', 'K'] + [str(x) for x in range(2,11)]
                           for p in ['Treboles', 'Picas', 'Corazones', 'Diamantes']]
            shuffle(self.cartas)

    def mostrar_cartas(self, todas = False):
        if todas:
            for c in self.cartas:
                c.mostrar_carta()
        else:
            print("* de *")
            for c in self.cartas[1:]:
                c.mostrar_carta()

    def valor_mazo(self):
        valor = 0
        for c in self.cartas:
            valor += c.valor_carta()

        tiene_as = False
        for c in self.cartas:
            if c.valor == 'A':
                tiene_as = True
                break
        if tiene_as and valor <= 11:
            valor += 10

        return valor

    def entregar_carta(self):
        if self.cartas != []:
            carta = self.cartas[0]
            self.cartas = self.cartas[1:]
        else:
            carta = Carta('0', 'Comodin')
        return carta

    def agregar_carta(self, carta):
        self.cartas.append(carta)

if __name__ == '__main__':

    m = Mazo(True)
    m.cartas = [Carta("5", "Picas"), Carta("A", "Diamantes"),
                Carta("A", "Treboles")]
    m.mostrar_cartas(True)
    
    print(m.valor_mazo())

    c = m.entregar_carta()
    c.mostrar_carta()
    print()
    m.mostrar_cartas(True)
    print()
    m.agregar_carta(c)
    m.mostrar_cartas(True)
