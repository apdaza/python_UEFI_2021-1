from libreria_picas_y_fijas import *
from util import astr

archivo = open('resultados.txt', 'w')

digitos = 3
intentos = 0 
secreto = generar_secreto(digitos)
print(secreto)
archivo.write("numero secreto %s \n" % astr(secreto))


while True:
    intentos += 1
    numero = capturar_numero(digitos)
    archivo.write("numero capturado %s \n" % astr(numero))
    resultado = comparar(secreto, numero)
    print("intento %d (picas = %d, fijas = %d)" % (intentos, resultado[0], resultado[1]))
    archivo.write("intento %d (picas = %d, fijas = %d) \n" % (intentos, resultado[0], resultado[1]))
    if resultado[1] == digitos:
        print("felicitaciones")
        archivo.write("felicitaciones \n")
        break
    if intentos == digitos * 2:
        print("se terminaron los intentos")
        archivo.write("se terminaron los intentos \n")
        break
    
archivo.close()
