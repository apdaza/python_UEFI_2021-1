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
                           for v in ['A', 'J', 'Q', 'K'] + [str(x) for x in range(1,11)]
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

        return valor

if __name__ == '__main__':

    c = Carta('Q', 'Diamantes')
    c.mostrar_carta()
    print(c.valor_carta())

    m = Mazo(True)
    m.cartas = [Carta("10", "Picas"), Carta("A", "Diamantes")]
    m.mostrar_cartas()
    print(m.valor_mazo())
