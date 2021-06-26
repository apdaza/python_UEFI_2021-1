def saludar(nombre, saludo = "Hola"):
    print(saludo + " " + nombre)


def saludar_grupo(nombres):
    for n in nombres:
        saludar(n, "Buenas tardes")

def saludar2(*nombres):
    for n in nombres:
        print("te saludo " + n)

def mostrar_parametros(**parametros):
    for parametro, valor in parametros.items():
        print(parametro, " = ", valor)
    

saludar('alejandro', 'Buen día')

saludar_grupo(['alejandro','marcela'])

saludar('Liliana')

saludar2('alejandro')
saludar2('alejandro', 'marcela', 'miguel')
saludar2('alejandro', 'marcela', 'miguel','marcela', 'miguel')

mostrar_parametros(nombre='alejandro', saludo='hola', edad='48')

mostrar_parametros(nombre='alejandro', edad=48, equipo = 'america')
