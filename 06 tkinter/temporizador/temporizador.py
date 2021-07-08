from unidad import UnidadDeTiempo

class Temporizador:
    def __init__(self):
        self.hora = UnidadDeTiempo(23)
        self.minuto = UnidadDeTiempo()
        self.segundo = UnidadDeTiempo()

        self.parado = True

    def retroceder(self):
        self.segundo.retroceder()
        if self.segundo.valor == self.segundo.tope:
            self.minuto.retroceder()
            if self.minuto.valor == self.minuto.tope:
                self.hora.retroceder()

        if self.segundo.valor == self.minuto.valor == self.hora.valor == 0:
            self.parado = True

    def borrar(self):
        self.hora.borrar()
        self.minuto.borrar()
        self.segundo.borrar()

        self.parado = True

    def cambiar_estado(self):
        self.parado = not self.parado

    def iniciar_valores(self, tiempo):
        self.hora.valor = tiempo[0]
        self.minuto.valor = tiempo[1]
        self.segundo.valor = tiempo[2]

    def retornar_tiempo(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hora.valor,
                                             self.minuto.valor,
                                             self.segundo.valor)
if __name__ == '__main__':
    c = Temporizador()
    c.cambiar_estado()
    c.segundo.valor = 40
    for i in range(100):
        c.retroceder()
        print(c.retornar_tiempo())
        if c.parado:
            break



    
