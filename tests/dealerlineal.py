import random 

cantidad = random.randint(1,10)
perder = False
while not perder:
    print(f"el dealer tiene: {cantidad}")
    cantidad += random.randint(1,10)
    if cantidad > 16:
        perder = True
        print(f"el dealer tiene: {cantidad}")
        