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

for i in range(5000):
    nombres.append('persona_' + str(i))
    edades.append(randint(20, 70))
    generos.append(choice(tipos_generos))
    ciudades.append(choice(nombres_ciudades))
    hijos.append(randint(0, 5))
    mascotas.append(randint(0, 5))

data = {'nombres': nombres,
        'edades': edades,
        'generos': generos,
        'ciudades': ciudades,
        'hijos': hijos,
        'mascotas': mascotas
    }

df = DataFrame(data, columns = ['nombres','edades','generos','ciudades',
                                'hijos','mascotas'])

print(df.head())

df.to_csv('info.csv')
