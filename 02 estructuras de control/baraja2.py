from random import shuffle

pintas = ['picas', 'treboles', 'corazones', 'diamantes']
valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

baraja = [(v, p) for v in valores for p in pintas]

shuffle(baraja)
"""
for carta in baraja:
    print(carta)
"""


ganadoras = ['diamantes', 'corazones']

while True:
    ganador_uno = False
    ganador_dos = False

    while not ganador_uno and not ganador_dos:
        carta_uno = baraja.pop()
        carta_dos = baraja.pop()
        
        print(carta_uno, carta_dos)
        if carta_uno[1] in ganadoras:
            ganador_uno = True
            
        if carta_dos[1] in ganadoras:
            ganador_dos = True

        
    if ganador_uno and ganador_dos:
        print("Empate")
    elif ganador_uno:
        print("gana jugador uno")
    else:
        print("gana jugador dos")

    if len(baraja) == 0:
        break

    if input("Desea continuar (n - para salir): ") == "n":
        break
