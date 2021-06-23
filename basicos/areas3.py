from math import sqrt, pi

punto1 = input("Ingrese las coordenadas del punto 1 separadas por coma: ")
coordenadas_uno = [int(x.strip(" ")) for x in punto1.split(",")]

punto2 = input("Ingrese las coordenadas del punto 2 separadas por coma: ")
coordenadas_dos = [int(x.strip(" ")) for x in punto2.split(",")]

radio = sqrt((coordenadas_uno[0]-coordenadas_dos[0])**2 +
             (coordenadas_uno[1]-coordenadas_dos[1])**2)

area = int(radio * pi ** 2)

print("el area de la circunferencia es " + str(area)) 
