from statistics import *

class Datos:

    def __init__(self, archivo):
        self.archivo = archivo

    def generar_matriz(self):
        f = open(self.archivo)
        lineas = f.readlines()
        f.close()
        lineas = [x.strip('\n') for x in lineas]
        self.matriz = [x.split(',') for x in lineas]
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz[f])):
                if f > 0:
                    self.matriz[f][c] = int(self.matriz[f][c])
        self.columnas = len(self.matriz[0])

    def calcular_promedio(self):
        for linea in self.matriz[1:]:
            linea.append(mean(linea[:self.columnas]))
        self.matriz[0].append("mean")

    def calcular_mediana(self):
        for linea in self.matriz[1:]:
            linea.append(median(linea[:self.columnas]))
        self.matriz[0].append("median")

    def calcular_moda(self):
        for linea in self.matriz[1:]:
            linea.append(mode(linea[:self.columnas]))
        self.matriz[0].append("mode")

    def generar_resultados(self, archivo):
        f = open(archivo, 'w')
        for linea in self.matriz:
            cadena = ""
            for dato in linea:
                cadena += str(dato) + ","
            cadena = cadena[:-1] + "\n"
            f.write(cadena)
        f.close()

if __name__ == '__main__':

    datos = Datos("datos.csv")
    datos.generar_matriz()
    datos.calcular_mediana()
    datos.calcular_promedio()
    datos.calcular_moda()
    datos.generar_resultados("resultados01.csv")

    
