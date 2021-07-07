from tkinter import Tk, Radiobutton, StringVar

def operacion():
    print(str_valor.get())

ventana = Tk()

str_valor = StringVar()
rb_1 = Radiobutton(ventana, text = "opcion 1", value = 1,
                        variable = str_valor, command = operacion)
rb_1.pack()

rb_2 = Radiobutton(ventana, text = "opcion 2", value = 2,
                        variable = str_valor, command = operacion)
rb_2.pack()

ventana.mainloop()
