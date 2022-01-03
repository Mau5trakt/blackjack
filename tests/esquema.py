import random
import os 


def inicio(numero):
    print(f"El Dealer tiene: {numero}")
    pass

def dealer(numero):
    dcantidad = numero
    perder = False
    while not perder:
        print (f"el dealer tiene: {dcantidad}")
        dcantidad += random.randint(1,10)
        if dcantidad > 16:
            perder = True

    print (f"el dealer tiene: {dcantidad}")
    return dcantidad


def j1():
    cantidad = random.randint(1,10)
    otra_carta = ""
    while cantidad < 21:
        print(f"tienes: {cantidad}")
        otra_carta = input("¿Desea otra carta?: \n")
        if otra_carta == "s":
            cantidad += random.randint(1,10)
        else:
            print(f"Su cantidad es: {cantidad} fin jugador 1")
            break


    if cantidad > 21:
        print(f"{cantidad}\n Perdiste")
    return cantidad



def main():
    numero = random.randint(1,10)
    inicio(numero)
    cantidad_jugador = j1()

    #TODO hacer por aparte los casos ganadores (lineal) y probarlos y hacer el sistema del dinero
    
    if cantidad_jugador > 21:
        exit()
    cantidad_dealer = dealer(numero)
    print(f"Jugador: {cantidad_jugador}, Dealer: {cantidad_dealer}")

    if cantidad_dealer > 21 & cantidad_jugador < 21:
        print("ganaste")
        exit()
    
    if cantidad_jugador > cantidad_dealer:
        print("Ganaste")
        exit()

    if cantidad_jugador < cantidad_dealer:
        print("Perdiste")
        exit()





if __name__ == "__main__":
    main()