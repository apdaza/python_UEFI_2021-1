from pandas import *
from random import randint, choice

nombres_ciudades = ['Bogotá', 'Chía', 'Zipaquirá', 'Cajicá', 'Cota']
tipos_generos = ['M','F']

nombres = []
edades = []
generos = []
ciudades = []
hijos = []
mascotas = []
vehiculos = []
salario = []

for i in range(10000):
    nombres.append('persona_' + str(i))
    edades.append(randint(20, 70))
    generos.append(choice(tipos_generos))
    ciudades.append(choice(nombres_ciudades))
    hijos.append(randint(0, 3))
    mascotas.append(randint(0, 10))
    vehiculos.append(randint(0,2))
    salario.append(randint(900, 7000))

data = {'nombres': nombres,
        'edades': edades,
        'generos': generos,
        'ciudades': ciudades,
        'hijos': hijos,
        'mascotas': mascotas,
        'vehiculos': vehiculos,
        'salario': salario
    }

df = DataFrame(data, columns = ['nombres','edades','generos','ciudades',
                                'hijos','mascotas','vehiculos','salario'])

print(df.head())

df.to_csv('info.csv')
