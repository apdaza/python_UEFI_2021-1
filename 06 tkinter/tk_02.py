from tkinter import Tk, Button

def saludar():
    print("hola mundo")
    
root = Tk()
boton = Button(root, text="saludar", command=saludar)
boton.pack()
root.mainloop()
