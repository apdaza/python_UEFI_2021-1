from tkinter import *

class GUI(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.init_gui()

    def init_gui(self):
        self.parent.title("Una ventana")


principal = Tk()
principal.geometry("500x500")
ventana = GUI(principal)
ventana.mainloop()
