from math import sqrt

punto1 = input("Ingrese las coordenadas del punto 1 separadas por coma: ")
coordenadas_uno = [int(x.strip(" ")) for x in punto1.split(",")]

punto2 = input("Ingrese las coordenadas del punto 2 separadas por coma: ")
coordenadas_dos = [int(x.strip(" ")) for x in punto2.split(",")]

coordenada_temporal = [coordenadas_uno[0], coordenadas_dos[1]]

distancia_x = sqrt((coordenadas_uno[0]-coordenada_temporal[0])**2 +
                   (coordenadas_uno[1]-coordenada_temporal[1])**2)

distancia_y = sqrt((coordenadas_dos[0]-coordenada_temporal[0])**2 +
                   (coordenadas_dos[1]-coordenada_temporal[1])**2)

area = int(distancia_x * distancia_y)

print("el area de la figura es " + str(area)) 
