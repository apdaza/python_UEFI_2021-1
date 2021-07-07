from tkinter import *

class AppHolaMundo:
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.frame.pack()

        self.etiqueta = Label(self.frame, text="Mi primera app con tk")
        self.etiqueta.pack()

        self.cadena = StringVar()
        self.texto = Entry(self.frame, textvariable = self.cadena)
        self.texto.pack(side=LEFT)

        self.boton = Button(self.frame, text = "Aceptar", command = self.saludar)
        self.boton.pack(side=RIGHT)

    def saludar(self):
        valor = self.cadena.get()
        if valor != "":
            self.cadena.set("Hola " + valor)
        else:
            self.cadena.set("Ingresa el nombre por favor")


principal = Tk()
app = AppHolaMundo(principal)
principal.mainloop()
