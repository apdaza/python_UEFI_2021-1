def suma_procedimiento(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)

def suma_funcion(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def incrementar(valor):
    return valor + 1

if __name__ == '__main__':
    suma_procedimiento(5, 6)
    res = suma_funcion(5, 6)
    print(res)

    numero = int(input("ingrese un número: "))

    valor = incrementar(numero)
    print(valor)

    numero = numero + 1
    print(numero)


