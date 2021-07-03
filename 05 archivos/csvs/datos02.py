from random import randint

titulos = []
for i in range(10):
    titulos.append("valor_"+str(i+1))

matriz = [titulos]

for i in range(500):
    lista = []
    for c in range(10):
        lista.append(randint(0, 10))
    matriz.append(lista)

f = open("datosos02.csv", 'w')
for linea in matriz:
    cadena = ""
    for dato in linea:
        cadena += str(dato) + ","
    cadena = cadena[:-1] + "\n"
    f.write(cadena)
f.close()
