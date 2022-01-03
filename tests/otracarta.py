import random

def mazo():
    colores = ["corazones", "diamantes", "picas", "tréboles"]
    baraja = []
    for color in colores:
        for carta in range(1, 15):
            id = carta
            card =([carta, "de", color])
            baraja.append(card)
    return baraja


def cartas(baraja):
    carta = random.choice(baraja)
    return carta



def main():
    UserCards = []
    baraja = mazo()
    UserCards.append(cartas(baraja))
    print(UserCards)
    

if __name__ == "__main__":
    main()