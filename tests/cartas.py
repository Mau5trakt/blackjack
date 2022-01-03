import random

colores = ["corazones", "diamantes", "picas", "tréboles"]
baraja = []
for color in colores:
    for carta in range(1, 15):
        id = carta
        card =([carta, "de", color])
        baraja.append(card)


print(f"Hola, tu carta es: {random.choice(baraja)} y {random.choice(baraja)}")