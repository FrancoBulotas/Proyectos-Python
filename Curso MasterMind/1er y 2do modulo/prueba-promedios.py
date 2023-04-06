import random

cara = 0
cara_mayor = 0
cruz = 0
cruz_mayor = 0
iguales = 0
i = 0
x = 0

while x < 100:
    while i < 10000:
        promedio = random.randint(0, 1)
        if promedio == 0:
            cara += 1
        elif promedio == 1:
            cruz += 1
        i += 1

    if cara > cruz:
        cara_mayor += 1
    elif cruz > cara:
        cruz_mayor += 1
    elif cara == cruz:
        iguales += 1

    if i == 10000:
        i = 0
        cara = 0
        cruz = 0
    x += 1

print("Cara fue mayor a cruz {} veces" .format(cara_mayor))
print("Cruz fue mayor a cara {} veces" .format(cruz_mayor))
print("Fueron iguales {} veces" .format(iguales))



