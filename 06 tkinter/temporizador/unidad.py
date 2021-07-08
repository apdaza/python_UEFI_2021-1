class UnidadDeTiempo:
    def __init__(self, tope = 59):
        self.valor = 0
        self.tope = tope

    def retroceder(self):
        if self.valor > 0:
            self.valor -= 1
        else:
            self.valor = self.tope

    def borrar(self):
        self.valor = 0

if __name__ == '__main__':

    u = UnidadDeTiempo(11)
    u.valor = 10
    for i in range(30):
        u.retroceder()
        print(u.valor)

    u.borrar()
    print(u.valor)
