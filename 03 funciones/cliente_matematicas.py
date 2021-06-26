from libreria_matematicas import suma, resta, potencia

print(suma(3, 4))
print(resta(3, 4))
print(potencia(3, 3))

print(suma(resta(3, 2), potencia(3, 2)))

r = resta(3, 2)
p = potencia(3, 2)
print(suma(r, p))
