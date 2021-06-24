tope = int(input("ingrese el tope: "))

for n in range(1, tope + 1, 3):
    print(n)

nombre = input("Ingrese su nombre: ")

for c in nombre:
    print(c)

for i in range(len(nombre)):
    print(i, nombre[i])
