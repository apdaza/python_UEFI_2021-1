from tkinter import Tk, Checkbutton, IntVar

def operacion():
    print(int_valor.get())

ventana = Tk()

int_valor = IntVar()
ckb_boton = Checkbutton(ventana, text = "prueba", variable = int_valor, command = operacion)
ckb_boton.pack()

ventana.mainloop()
