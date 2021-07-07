from tkinter import Tk, Button, Entry

def saludar():
    print("hola mundo")
    
root = Tk()
texto = Entry(root)
texto.pack()
boton = Button(root, text="saludar", command=saludar)
boton.pack()
root.mainloop()
