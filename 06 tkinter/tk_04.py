from tkinter import Tk, Button, Entry, Label

def saludar():
    print("hola mundo")
    
root = Tk()

etiqueta = Label(root, text="Nombre:")
etiqueta.pack()

texto = Entry(root)
texto.pack()

boton = Button(root, text="saludar", command=saludar)
boton.pack()

root.mainloop()
