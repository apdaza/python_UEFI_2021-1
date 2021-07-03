def average(elementos):
    return sum(elementos)/len(elementos)

# cargar el archivo
f = open("datos.csv")
# lectura de sus lineas
lineas = f.readlines()
# cerramos el archivo
f.close()

#eliminamos el salto de linea
lineas = [x.strip('\n') for x in lineas]

#separar los valores
matriz = [x.split(',') for x in lineas]

# convertir a enteros cada dato desde la fila 1
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        if f > 0:
            matriz[f][c] = int(matriz[f][c])

#agregamos la columna suma
for linea in matriz[1:]:
    linea.append(sum(linea))
matriz[0].append("suma")

#agregamos la columna minimo
for linea in matriz[1:]:
    linea.append(min(linea))
matriz[0].append("minimo")

#agregamos la columna maximo
for linea in matriz[1:]:
    linea.append(max(linea[:-2]))
matriz[0].append("maximo")

#agregamos la columna maximo
for linea in matriz[1:]:
    linea.append(average(linea[:-3]))
matriz[0].append("average")

#imprimimos como matriz
for linea in matriz:
    for dato in linea:
        print(dato, end="\t")
    print()

f = open("resultados.csv", 'w')
for linea in matriz:
    cadena = ""
    for dato in linea:
        cadena += str(dato) + ","
    cadena = cadena[:-1] + "\n"
    f.write(cadena)
f.close()
