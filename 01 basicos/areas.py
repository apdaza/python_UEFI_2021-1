punto1 = input("Ingrese las coordenadas del punto 1 separadas por coma: ")
coordenadas_uno = [int(x.strip(" ")) for x in punto1.split(",")]
"""
temporal1 = punto1.split(",")
for indice in range(len(temporal1)):
    temporal1[indice] = temporal1[indice].strip(" ")
for indice in range(len(temporal1)):
    temporal1[indice] = int(temporal1[indice])
"""    
punto2 = input("Ingrese las coordenadas del punto 2 separadas por coma: ")
coordenadas_dos = [int(x.strip(" ")) for x in punto2.split(",")]

coordenada_temporal = [coordenadas_uno[0], coordenadas_dos[1]]
print(coordenadas_uno, coordenadas_dos, coordenada_temporal)

distancia_x = coordenadas_dos[0] - coordenada_temporal[0]
distancia_y = coordenadas_uno[1] - coordenada_temporal[1]

print(distancia_x, distancia_y)

area = distancia_x * distancia_y

print(area)
