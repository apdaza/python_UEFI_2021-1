"""
open(nombre_archivo, modo)

open(nombre_archivo, 'r') -> solo lectura -> error si el archivo no existe
open(nombre_archivo, 'w') -> modo de escritura -> crea el archivo si no existe
open(nombre_archivo, 'a') -> agrega contenido al archivo -> crear el archiv si no existe
open(nombre_archivo, 'x') -> crea el archivo -> error si el archivo existe
"""
from os import path, remove

f = open('demo.txt')
print(f.read())
f.close()

f = open('fuentes/fuentes_demo.txt', 'r')
print(f.read())
f.close()

f = open('../ejercicios_demo.txt', 'r')
print(f.read())
f.close()

f = open('../otras_fuentes/otras_demo.txt', 'r')
print(f.read())
f.close()

# no se recomienda usar rutas absolutas
f = open('/home/alejandro/Escritorio/raiz_demo.txt', 'r')
print(f.read())
f.close()

f = open('demo_escritura.txt', 'w')
f.write("escritura a un archivo \n")
f.write("desde python")
f.close()

f = open('demo_escritura.txt')
print(f.read())
f.close()

if path.exists("archivo_creado.txt"):
    print("el archivo ya existe")
else:
    f = open("archivo_creado.txt", 'x')

if path.exists("archivo_creado"):
    remove("archivo_creado")
else:
    print("el archivo no existe")

f = open("archivo_creado.txt", 'a')
f.write("linea agregada \n")
f.close()

f = open('demo.txt')
for c in f:
    print(c)
f.close()

f = open('demo.txt')
lineas = f.readlines()
print(lineas[:-1])
f.close()
