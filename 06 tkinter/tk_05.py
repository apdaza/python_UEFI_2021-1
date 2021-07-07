from tkinter import *

def saludar():
    nombre = str_nombre.get()
    str_saludo.set("hola mundo " + nombre)
    
root = Tk()

etiqueta = Label(root, text="Nombre:")
etiqueta.pack()

str_nombre = StringVar()
texto = Entry(root, textvariable = str_nombre)
texto.pack()

boton = Button(root, text="saludar", command=saludar)
boton.pack()

str_saludo = StringVar()
etiqueta_saludo = Label(root, textvariable = str_saludo)
etiqueta_saludo.pack()

root.mainloop()
