from tkinter import *

def saludar():
    nombre = str_nombre.get()
    str_saludo.set("hola mundo " + nombre)

def borrar():
    str_nombre.set("")
    str_saludo.set("")
    
root = Tk()
root.geometry("400x300")

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

boton_borrar = Button(root, text="borrar", command=borrar)
boton_borrar.pack()

root.mainloop()
