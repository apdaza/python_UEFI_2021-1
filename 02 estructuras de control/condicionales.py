x = int(input("ingrese un valor: "))

print("usted ingreso el: " + str(x))

if x % 2 == 0:
    print("el número ingresado es par")
elif x % 3 == 0:
    print("El número ingresado es múltiplo de 3")
elif x % 5 == 0:
    print("El número ingresado es múltiplo de 5")
else:
    print("el número ingresado no cumple con las evaluaciones")

print()

if x % 2 == 0:
    print("el número ingresado es par")
if x % 3 == 0:
    print("El número ingresado es múltiplo de 3")
if x % 5 == 0:
    print("El número ingresado es múltiplo de 5")
if x % 2 != 0 or x % 3 != 0 or x % 5 != 0:
    print("el número ingresado no cumple con las evaluaciones")
