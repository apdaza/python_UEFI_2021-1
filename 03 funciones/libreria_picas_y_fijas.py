from random import randint

def generar_secreto(digitos):
    secreto = []
    while True:
        n = randint(0,9)
        if n not in secreto:
            secreto.append(n)
        if len(secreto) == digitos:
            break
    return secreto

def capturar_numero(digitos):
    while True:
        numero = []
        usuario = input("Ingrese un numero de %d digitos: " % digitos)
        for u in usuario:
            if int(u) not in numero:
                numero.append(int(u))
        if len(numero) == digitos:
            break
    return numero

def comparar(secreto, usuario):
    picas = 0
    fijas = 0

    for i in range(len(secreto)):
        for j in range(len(usuario)):
            if secreto[i] == usuario[j]:
                if i == j:
                    fijas += 1
                else:
                    picas += 1
    return picas, fijas


