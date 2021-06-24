from random import randint
# preguntamos con cuantos digitos
while True:
    digitos = int(input("Seleccione la cantidad de digitos: "))
    if digitos in [2,3,5]:
        break
    else:
        print("cantidad de digitos no valida")
# generamos el numerom secreto
secreto = []
while True:
    n = randint(0, 9)
    if n not in secreto:
        secreto.append(n)
    if len(secreto) == digitos:
        break
print(secreto)

#vamos a adivinar el numero
intentos = 0
while True:
    while True:
        n = input("Ingrese su número: ")
        numero = [int(c) for c in n]
        validado = []
        for i in numero:
            if i not in validado:
                validado.append(i)
        if len(validado) == digitos:
            break

    picas = 0
    fijas = 0

    for i in range(len(secreto)):
        for j in range(len(validado)):
            if secreto[i] == validado[j]:
                if i == j:
                    fijas += 1
                else:
                    picas += 1

    print("tienes %d picas y %d fijas" % (picas, fijas))
    intentos += 1
    if fijas == len(secreto):
        print("Felicitaciones")
        break
    if intentos == len(secreto)*2:
        print("máximos intentos jugados")
        break
    if input("Desea continuar (n - para salir): ") == "n":
        print("Gracias por jugar")
        break
    
