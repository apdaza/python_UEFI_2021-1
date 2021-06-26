from libreria_figuras import *

print("Primer punto")
punto1 = capturar_punto()
print("Segundo punto")
punto2 = capturar_punto()

area = area_rectangulo(punto1, punto2)
print(area)

perimetro = perimetro_rectangulo(punto1, punto2)
print(perimetro)

area = area_circulo(punto1, punto2)
print(area)

perimetro = perimetro_circulo(punto1, punto2)
print(perimetro)
