numero_uno = 15
numero_dos = 2
flotante_uno = 2.5
flotante_dos = 3.0
variable = "texto"

# para ver el tipo de las variables
print(type(numero_uno))
print(type(numero_dos))
print(type(variable))

# operamos sobre las variables
suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
producto = numero_uno * numero_dos
division_uno = numero_uno / numero_dos
division_dos = numero_uno // numero_dos
division_tres = flotante_uno / flotante_dos
potencia = numero_uno ** numero_dos
repeticion = variable * numero_dos
concatenado = variable + " - " + str(numero_dos)

print(suma, type(suma))
print(resta, type(resta))
print(producto, type(producto))
print(division_uno, type(division_uno))
print(division_dos, type(division_dos))
print(division_tres, type(division_tres))
print(potencia, type(potencia))
print(repeticion, type(repeticion))
print(concatenado, type(concatenado))

# nombres de variables validos
_mi_variable_ = "algo"
valor2 = 34
v5alor = 4

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

z = y = x = 25
print(z)
print(y)
print(x)

print(a, b)
a, b = b, a
"""
temp = a
a = b
b = temp
"""
print(a, b)

def mi_funcion():
    print("ejecutado en una funcion")

mi_funcion()

cadena = "esto es un texto en una variable"
print(cadena)
print(cadena[2])
print(cadena[-1])
print(cadena[4:10])
print(cadena[5:])
print(cadena[:-5])

nombre = input("ingrese su nombre completo")
nombres = nombre.split(" ")
print("primer nombre: " + nombres[0])
print("segundo nombre: " + nombres[1])
print("primer apellido: " + nombres[2])
print("segundo apellido: " + nombres[3])
