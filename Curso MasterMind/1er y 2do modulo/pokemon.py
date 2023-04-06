
from random import randint

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_pikachu > 0 and vida_squirtle > 0:
    # Se turnan para pelear

    # turno de pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    if vida_pikachu < 0:
       vida_pikachu = 0
    elif vida_squirtle < 0:
        vida_squirtle = 0

    barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
    print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu, " " * (100 - barra_de_vida_pikachu),
                                                vida_pikachu , VIDA_INICIAL_PIKACHU))

    barra_de_vida_squirtle = int(vida_squirtle * 100 / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:     [{}{}] [{}/{}]".format("*" * barra_de_vida_squirtle, " " * (100 - barra_de_vida_squirtle),
                                                vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar...\n\n")

    # Turno de squirtle
    print("Turno Squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("¿Que ataque deseas hacer? [P] Placaje, [A]Pistola Agua, [B]Burbuja, [N]Nada: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle no hace nada")
        vida_pikachu = vida_pikachu

    if vida_pikachu < 0:
       vida_pikachu = 0
    elif vida_squirtle < 0:
        vida_squirtle = 0

    barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
    print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu, " " * (100 - barra_de_vida_pikachu),
                                                vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_de_vida_squirtle = int(vida_squirtle * 100 / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:     [{}{}] [{}/{}]".format("*" * barra_de_vida_squirtle, " " * (100 - barra_de_vida_squirtle),
                                                vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar... \n\n")

if vida_pikachu > vida_squirtle:
    print("Pikachu gana")
else:
    print("Squirtle gana")


