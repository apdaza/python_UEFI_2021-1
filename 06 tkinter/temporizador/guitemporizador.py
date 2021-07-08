from tkinter import *
from temporizador import Temporizador
from threading import *
from time import sleep

class AppTemporizador(Thread):

    def __init__(self):
        self.principal = Tk()
        self.crono = Temporizador()
        self.frame = Frame(self.principal)
        self.frame.pack()

        self.valor = StringVar()
        self.display = Entry(self.frame, textvariable = self.valor,
                             font = ('Helvetica', 20), justify=RIGHT)
        self.display.pack(side=TOP, padx=10, pady=10)

        self.valor.set(self.crono.retornar_tiempo())

        self.boton_iniciar = Button(self.frame, text = 'Iniciar/Parar',
                                    command = self.cambiar_estado)
        self.boton_iniciar.pack(side=LEFT, padx=10, pady=10)

        self.boton_borrar = Button(self.frame, text = 'Borrar',
                                   command = self.borrar)
        self.boton_borrar.pack(side=RIGHT, padx=10, pady=10)

        Thread.__init__(self)
        self.start()

        self.principal.mainloop()

    def cambiar_estado(self):
        tiempo = [int(x) for x in self.valor.get().split(":")]
        self.crono.iniciar_valores(tiempo)
        self.crono.cambiar_estado()

    def borrar(self):
        self.crono.borrar()
        self.valor.set(self.crono.retornar_tiempo())

    def run(self):
        while True:
            if not self.crono.parado:
                self.crono.retroceder()
                sleep(0.5)
                self.valor.set(self.crono.retornar_tiempo())

    def callback(self):
        self.principal.quit()

if __name__ == '__main__':
    app = AppTemporizador()
