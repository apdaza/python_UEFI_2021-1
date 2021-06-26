from math import sqrt, pi

def capturar_punto():
    x = int(input("Ingrese el valor de x del punto: "))
    y = int(input("Ingrese el valor de y del punto: "))
    return x, y

def calcular_distancia(punto1, punto2):
    return sqrt(((punto1[0] - punto2[0]) ** 2) +
                ((punto1[1] - punto2[1]) ** 2))


def area_rectangulo(punto1, punto2):
    punto3 = punto1[0], punto2[1]
    lado1 = calcular_distancia(punto1, punto3)
    lado2 = calcular_distancia(punto2, punto3)
    area = lado1 * lado2
    return area

def perimetro_rectangulo(punto1, punto2):
    punto3 = punto1[0], punto2[1]
    lado1 = calcular_distancia(punto1, punto3)
    lado2 = calcular_distancia(punto2, punto3)
    perimetro = lado1 * 2 + lado2 * 2
    return perimetro

def area_circulo(punto1, punto2):
    radio = calcular_distancia(punto1, punto2)
    area = pi * radio ** 2
    return area

def perimetro_circulo(punto1, punto2):
    radio = calcular_distancia(punto1, punto2)
    perimetro = 2 * pi * radio
    return perimetro


    
