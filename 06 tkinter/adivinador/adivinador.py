from tkinter import *
from random import randint

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.title("Aplicación")
        parent.configure(width=200, height=200)
        self.place(relwidth=1, relheight=1)

        self.valor = StringVar()
        self.texto = Entry(self, textvariable=self.valor)
        self.texto.place(x=10, y=10)

        self.boton = Button(self, text="verificar", command=self.verificar)
        self.boton.place(x=100, y=60)

        self.msg = StringVar()
        self.display = Label(self, textvariable = self.msg)
        self.display.place(x=10, y=90)
        
        self.secreto = randint(0,99)
        

    def verificar(self):
        if int(self.valor.get()) > self.secreto:
            self.msg.set("mas bajo por favor")
        elif int(self.valor.get()) < self.secreto:
            self.msg.set("mas alto por favor")
        else:
            self.msg.set("felicitaciones")
        

principal = Tk()
app = App(principal)
principal.mainloop()

