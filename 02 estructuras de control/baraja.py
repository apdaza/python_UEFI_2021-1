from random import shuffle

pintas = ['picas', 'treboles', 'corazones', 'diamantes']
valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

baraja = [(v, p) for v in valores for p in pintas]

shuffle(baraja)
"""
for carta in baraja:
    print(carta)
"""
no_ganador = True

while no_ganador:
    carta_uno = baraja.pop()
    carta_dos = baraja.pop()

    print(carta_uno, carta_dos)
    if carta_uno[0] == 'A':
        no_ganador = False
        print("gana jugador 1")
        
    if carta_dos[0] == 'A':
        no_ganador = False
        print("gana jugador 2")

    
