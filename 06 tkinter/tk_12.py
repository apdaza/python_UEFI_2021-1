from tkinter import *

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        parent.title("Aplicación")
        parent.configure(width=300, height=200)
        self.place(relwidth=1, relheight=1)

        self.boton = Button(self, text="Hola")
        self.boton.place(x=160, y=40)


principal = Tk()
app = App(principal)
principal.mainloop()
