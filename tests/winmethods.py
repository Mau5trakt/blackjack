import random

def winmethods(jugador, casa):
    if jugador > 21:
        print("Perdiste")
    elif casa > 21: 
        print("ganaste")
    elif jugador > casa:
        print("ganaste")
    elif casa > jugador: 
        print("Perdiste")
    elif casa == jugador: 
        print("Empate")


for n in range (2000):
    b = random.randint(15,21)
    a = random.randint(15,30)
    print(f"jugador: {a}, casa: {b}")
    winmethods(a,b)