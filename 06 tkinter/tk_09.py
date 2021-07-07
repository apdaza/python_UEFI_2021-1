from tkinter import *

# función que genera una nueva ventana
def nueva_ventana():
    #instancia de una ventana en el top de presentación
    nueva = Toplevel(principal) 
    nueva.title("Ventana nueva") # seteamos el titulo de la ventana
    nueva.geometry("400x400") # definimos la geometría
    nueva.focus_set() # asignamos el foco
    boton = Button(nueva, text="no hago nada") # define un boton
    boton.pack() # se hace el pack del boton para que sea visible

# instanciamos la ventana principal
principal = Tk()
#definimos su geometría
principal.geometry("640x480")
# creamos un bpotón y lo linkeamos al la función
boton = Button(principal, text="Abrir ventana nueva", command = nueva_ventana)
boton.pack() # se empaquet el botón
# se genera el mainloop para activar la ventana
principal.mainloop()
