import random
import os 


def inicio(numero):
    print(f"El Dealer tiene: {numero}")
    pass

def dealer(numero, cantidad_jugador):
    dcantidad = numero
    perder = False
    while not perder and dcantidad < cantidad_jugador:
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

def winmethods(cantidad_jugador, cantidad_dealer):
    perder = "Perdiste"
    ganar = "Ganaste"
    empate = "Empate"
    if cantidad_jugador > 21:
        print(perder)
        resultado = perder
        return resultado
    elif cantidad_dealer > 21:
        print(ganar)
        resultado = ganar
        return resultado
    elif cantidad_jugador > cantidad_dealer:
        print(ganar)
        resultado = ganar
        return resultado
    elif cantidad_dealer > cantidad_jugador:
        print(perder)
        resultado = perder
        return resultado
    elif cantidad_jugador == cantidad_dealer: 
        print(empate)
        resultado = empate
        return resultado


def modificar(resultado):
    f = open("stats.txt", "r")
    documento_en_lista = f.readlines()
    ganadas = documento_en_lista[0]
    perdidas = documento_en_lista[1]
    empates = documento_en_lista[2]
    if resultado == "Ganaste":
        numero_ganadas = int(ganadas[8:])
        numero_ganadas += 1
        neoganadas = 'Ganadas: '+ str(numero_ganadas)
        with open('stats.txt', 'w') as file: 
            file.write(neoganadas)
            file.write('\n')
            file.write(perdidas)
            file.write(empates)
            file.close()
    elif resultado == "Perdiste":
        numero_perdidas = int(perdidas[9:])
        numero_perdidas += 1
        neoperdidas = 'Perdidas: '+ str(numero_perdidas)
        with open('stats.txt', 'w') as file:
            file.write(ganadas)
            file.write(neoperdidas)
            file.write('\n')
            file.write(empates)
            file.close()
    else:
        numero_empates = int(empates[8:])
        numero_empates += 1
        neoempates = 'Empates: '+ str(numero_empates)
        with open('stats.txt', 'w') as file:
            file.write(ganadas)
            file.write(perdidas)
            file.write(neoempates)
            file.close()

    


def main():
    numero = random.randint(1,10)
    inicio(numero)
    cantidad_jugador = j1()
    cantidad_dealer = dealer(numero, cantidad_jugador)
    resultado = winmethods(cantidad_jugador, cantidad_dealer) # * Control del retorno de la función
    modificar(resultado)

    #TODO hacer por aparte los casos ganadores (lineal) y probarlos y hacer el sistema del dinero





if __name__ == "__main__":
    main()