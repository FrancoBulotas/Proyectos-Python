# Adivinanza de numero

import random
num = random.randint(1, 10)
elegido = int(input("Adivine un numero del 1 al 10: "))

if elegido == num:
    print("Elegiste bien")

if elegido > 10:
    print("El numero es mayor a 10")

if elegido < 1:
    print("El numero es menor a 1")

print("Tu numero ganador era: {}".format(num))