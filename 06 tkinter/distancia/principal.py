from tkinter import *
from punto import Punto

class AppDistancia:

    def __init__(self, parent):
        self.p1 = Punto()
        self.p2 = Punto()
        self.frame = Frame(parent)
        self.frame.pack()

        self.label_punto1 = Label(self.frame, text = "Punto 1:",
                                  font = ("Helvetica", 30))
        self.label_punto1.pack()

        self.coordenadas1 = StringVar()
        self.texto_punto1 = Entry(self.frame, textvariable = self.coordenadas1,
                                  font = ("Helvetica", 30))
        self.texto_punto1.pack()

        self.label_punto2 = Label(self.frame, text = "Punto 2:",
                                  font = ("Helvetica", 30))
        self.label_punto2.pack()

        self.coordenadas2 = StringVar()
        self.texto_punto2 = Entry(self.frame, textvariable = self.coordenadas2,
                                  font = ("Helvetica", 30))
        self.texto_punto2.pack()

        self.distancia = StringVar()
        self.label_distancia = Label(self.frame, textvariable=self.distancia,
                                     font = ("Helvetica", 30))
        self.label_distancia.pack()

        self.boton = Button(self.frame, text="Calcular", command=self.calcular,
                            font = ("Helvetica", 30))
        self.boton.pack()

    def calcular(self):
        punto1 = [int(x) for x in self.coordenadas1.get().split(",")]
        punto2 = [int(x) for x in self.coordenadas2.get().split(",")]

        self.p1.x = punto1[0]
        self.p1.y = punto1[1]

        self.p2.x = punto2[0]
        self.p2.y = punto2[1]

        distancia = self.p1.calcular_distancia(self.p2)
        self.distancia.set(str(distancia))
                                     


principal = Tk()
app = AppDistancia(principal)
principal.mainloop()
