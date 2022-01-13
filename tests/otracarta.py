import random

def mazo():
    colores = ["corazones", "diamantes", "picas", "tréboles"]
    baraja = []
    for color in colores:
        for carta in range(1, 15):
            id = carta
            card =[carta, "de", color]
            baraja.append(card)
    return baraja


def cartas(baraja):
    carta = random.choice(baraja)
    return carta


def usercards(baraja):
    carta = random.choice(baraja)
    id = carta[0]
    idconvertido = int(id)
    if idconvertido > 10 and idconvertido < 14:
        idconvertido = 10
    print(carta, idconvertido)

def main():
    baraja = mazo()
    #print(baraja) # Mando a imprimir por completo el deck
    usercards(baraja)
#    carta = cartas(baraja)
#    print(carta)
#    id = carta[0]
    #print(id)


if __name__ == "__main__":
    main()