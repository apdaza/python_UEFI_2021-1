from tkinter import *
from punto import Punto
from figuras import *

class AppDistancia:

    def __init__(self, parent):
        self.p1 = Punto()
        self.p2 = Punto()
        self.frame = Frame(parent)
        self.frame.master.geometry("600x400")

        self.label_punto1 = Label(self.frame, text = "Punto 1:",
                                  font = ("Helvetica", 30))
        self.label_punto1.grid(row=0, column=0)

        self.coordenadas1 = StringVar()
        self.texto_punto1 = Entry(self.frame, textvariable = self.coordenadas1,
                                  font = ("Helvetica", 30))
        self.texto_punto1.grid(row=0, column=1)
        
        self.label_punto2 = Label(self.frame, text = "Punto 2:",
                                  font = ("Helvetica", 30))
        self.label_punto2.grid(row=1, column=0)

        self.coordenadas2 = StringVar()
        self.texto_punto2 = Entry(self.frame, textvariable = self.coordenadas2,
                                  font = ("Helvetica", 30))
        self.texto_punto2.grid(row=1, column=1)
        
        self.distancia = StringVar()
        self.label_distancia = Label(self.frame, textvariable=self.distancia,
                                     font = ("Helvetica", 30))
        self.label_distancia.grid(row=6, column=0, columnspan=2)

        self.boton = Button(self.frame, text="Calcular", command=self.calcular,
                            font = ("Helvetica", 30))
        self.boton.grid(row=7, column=1)

        self.opcion = StringVar()
        self.opcion1 = Radiobutton(self.frame, text = "distancia", value = 1,
                        variable = self.opcion, font = ("Helvetica", 30))
        self.opcion1.grid(row=2, column=1, columnspan=2, sticky='w')
        
        self.opcion2 = Radiobutton(self.frame, text = "circulo", value = 2,
                        variable = self.opcion, font = ("Helvetica", 30))
        self.opcion2.grid(row=3, column=1, columnspan=2, sticky='w')

        self.opcion3 = Radiobutton(self.frame, text = "rectangulo", value = 3,
                        variable = self.opcion, font = ("Helvetica", 30))
        self.opcion3.grid(row=4, column=1, columnspan=2, sticky='w')

        self.opcion.set(1)
        
        
        self.frame.grid(row=0, column=0)
        
    def calcular(self):
        punto1 = [int(x) for x in self.coordenadas1.get().split(",")]
        punto2 = [int(x) for x in self.coordenadas2.get().split(",")]

        self.p1.x = punto1[0]
        self.p1.y = punto1[1]

        self.p2.x = punto2[0]
        self.p2.y = punto2[1]

        if self.opcion.get() == "1":
            distancia = self.p1.calcular_distancia(self.p2)
            self.distancia.set(str(distancia))
        elif self.opcion.get() == "2":
            figura = Circulo(self.p1, self.p2)
            figura.calcular_area()
            self.distancia.set(str(figura.area))                         
        else:
            figura = Rectangulo(self.p1, self.p2)
            figura.calcular_area()
            self.distancia.set(str(figura.area))

principal = Tk()
app = AppDistancia(principal)
principal.mainloop()
