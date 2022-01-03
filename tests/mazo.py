import random



def mazo():
    baraja = []
    colores = ["corazones", "diamantes", "picas", "tréboles"]
    #for color in colores:
        #for carta in range (1, 15):
    for color in colores:
        for carta in range (1, 15):
                
            id = carta
            card =(carta, color)
            baraja.append(card)
    return baraja, id


def cartas(baraja):
    carta = random.choice(baraja)
    print(carta)
    return carta
    
    





def main():
    baraja = mazo()
    cartas(baraja)



if __name__ == "__main__":
    main()