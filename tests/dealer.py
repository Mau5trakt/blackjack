import random

def dealer():
    cantidad = random.randint(1,10)
    perder = False
    while not perder:
        print (f"el dealer tiene: {cantidad}")
        cantidad += random.randint(1,10)
        if cantidad > 16:
            perder = True

    print (f"el dealer tiene: {cantidad}")
    return cantidad

            



def main():
    cantidad = dealer()
    print(f"manipulando {cantidad}")


if __name__ == "__main__":
    main()