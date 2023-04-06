import os
import readchar
import random

import pikachu_VS_bulbasaur
import pikachu_VS_squirtle
import pikachu_VS_charizard

obstacle_definition = """\
##########################
                   #######
##############     #######
##############     #######
###                #######
###      #################
###             ##########
############# ############
#######          #########
############      ########
##########   ##   ########
#############      #######
############   ###   #####
################## #######
################      ####\
"""


POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 1

i = 0
my_position = [0, 1]
squirtle = [6, 1]
bulbasaur = [13, 7]
charizard = [18, 13]

# Creando obstaculo en el mapadd
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main Loop
while True:
    os.system("cls")

    # Crea mapa y Personaje
    print("|" + "-" * (MAP_WIDTH * 2) + "|")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            object_in_cell = None

            if squirtle[POS_X] == coordinate_x and squirtle[POS_Y] == coordinate_y:
                char_to_draw = "SQ"
                object_in_cell = squirtle

            if bulbasaur[POS_X] == coordinate_x and bulbasaur[POS_Y] == coordinate_y:
                char_to_draw = "BU"
                object_in_cell = bulbasaur

            if charizard[POS_X] == coordinate_x and charizard[POS_Y] == coordinate_y:
                char_to_draw = "CH"
                object_in_cell = charizard

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell == squirtle:
                    os.system("cls")
                    from random import randint
                    import os

                    VIDA_INICIAL_PIKACHU = 65
                    VIDA_INICIAL_SQUIRTLE = 70

                    vida_pikachu = VIDA_INICIAL_PIKACHU
                    vida_squirtle = VIDA_INICIAL_SQUIRTLE

                    while vida_pikachu > 0 and vida_squirtle > 0:
                        # Se turnan para pelear

                        # turno de Squirtle
                        print("Turno de Squirtle")
                        ataque_squirtle = randint(1, 2)
                        if ataque_squirtle == 1:
                            print("Squirtle ataca con Placaje")
                            vida_pikachu -= 10
                        else:
                            print("Squirtle ataca con Pistola de Agua")
                            vida_pikachu -= 11

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        elif vida_squirtle < 0:
                            vida_squirtle = 0

                        barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                                    " " * (100 - barra_de_vida_pikachu),
                                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_de_vida_squirtle = int(vida_squirtle * 100 / VIDA_INICIAL_SQUIRTLE)
                        print("Squirtle:     [{}{}] [{}/{}]".format("*" * barra_de_vida_squirtle,
                                                                    " " * (100 - barra_de_vida_squirtle),
                                                                    vida_squirtle, VIDA_INICIAL_SQUIRTLE))

                        input("Enter para continuar...\n")

                        if vida_pikachu == 0:
                            break
                        elif vida_squirtle == 0:
                            break

                        # Turno de Pikachu
                        print("Turno de Pikachu")
                        ataque_pikachu = None
                        while ataque_pikachu not in ["B", "O", "N"]:
                            ataque_pikachu = input(
                                "¿Que ataque deseas hacer? [B] Bola Voltio, [O] Onda Trueno, [N]Nada: ")
                        os.system("cls")
                        if ataque_pikachu == "B":
                            print("Pikachu ataca con Bola Voltio")
                            vida_squirtle -= 10
                        elif ataque_pikachu == "O":
                            print("Pikachu ataca con Onda Trueno")
                            vida_squirtle -= 14
                        elif ataque_pikachu == "N":
                            print("Pikachu no hace nada")
                            vida_squirtle = vida_squirtle

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        elif vida_squirtle < 0:
                            vida_squirtle = 0

                        barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                                    " " * (100 - barra_de_vida_pikachu),
                                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_de_vida_squirtle = int(vida_squirtle * 100 / VIDA_INICIAL_SQUIRTLE)
                        print("Squirtle:     [{}{}] [{}/{}]".format("*" * barra_de_vida_squirtle,
                                                                    " " * (100 - barra_de_vida_squirtle),
                                                                    vida_squirtle, VIDA_INICIAL_SQUIRTLE))
                        input("Enter para continuar... \n")

                    if vida_pikachu > vida_squirtle:
                        squirtle = [100, 100]
                        print("Le ganaste a Squirtle!")
                    elif vida_squirtle > vida_pikachu:
                        print("Perdiste! Squirtle te ganó")
                        exit()

                if object_in_cell == bulbasaur:
                    os.system("cls")
                    from random import randint
                    import os

                    VIDA_INICIAL_PIKACHU = 65
                    VIDA_INICIAL_BULBASAUR = 73

                    vida_pikachu = VIDA_INICIAL_PIKACHU
                    vida_bulbasaur = VIDA_INICIAL_BULBASAUR

                    while vida_pikachu > 0 and vida_bulbasaur > 0:
                        # Se turnan para pelear

                        # turno de bulbasaur
                        print("Turno de bulbasaur")
                        ataque_bulbasaur = randint(1, 2)
                        if ataque_bulbasaur == 1:
                            print("Bulbasaur ataca con Gruñido Growl")
                            vida_pikachu -= 9
                        else:
                            print("Bulbasaur ataca con Drenadoras Leech Seed")
                            vida_pikachu -= 12

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        elif vida_bulbasaur < 0:
                            vida_bulbasaur = 0

                        barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:     [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                                    " " * (100 - barra_de_vida_pikachu),
                                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_de_vida_bulbasaur = int(vida_bulbasaur * 100 / VIDA_INICIAL_BULBASAUR)
                        print("Bulbasaur:   [{}{}] [{}/{}]".format("*" * barra_de_vida_bulbasaur,
                                                                     " " * (100 - barra_de_vida_bulbasaur),
                                                                     vida_bulbasaur, VIDA_INICIAL_BULBASAUR))

                        input("Enter para continuar...\n")

                        if vida_pikachu == 0:
                            break
                        elif vida_bulbasaur == 0:
                            break

                        # Turno de Pikachu
                        print("Turno de Pikachu")
                        ataque_pikachu = None
                        while ataque_pikachu not in ["B", "O", "N"]:
                            ataque_pikachu = input(
                                "¿Que ataque deseas hacer? [B] Bola Voltio, [O] Onda Trueno, [N]Nada: ")
                        os.system("cls")
                        if ataque_pikachu == "B":
                            print("Pikachu ataca con Bola Voltio")
                            vida_bulbasaur -= 10
                        elif ataque_pikachu == "O":
                            print("Pikachu ataca con Onda Trueno")
                            vida_bulbasaur -= 14
                        elif ataque_pikachu == "N":
                            print("Pikachu no hace nada")
                            vida_bulbasaur = vida_bulbasaur

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        elif vida_bulbasaur < 0:
                            vida_bulbasaur = 0

                        barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:     [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                                    " " * (100 - barra_de_vida_pikachu),
                                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_de_vida_bulbasaur = int(vida_bulbasaur * 100 / VIDA_INICIAL_BULBASAUR)
                        print("Bulbasaur:   [{}{}] [{}/{}]".format("*" * barra_de_vida_bulbasaur,
                                                                     " " * (100 - barra_de_vida_bulbasaur),
                                                                     vida_bulbasaur, VIDA_INICIAL_BULBASAUR))
                        input("Enter para continuar... \n")

                    if vida_pikachu > vida_bulbasaur:
                        bulbasaur = [100, 100]
                        print("Le ganaste a Bulbasaur!")
                    elif vida_bulbasaur > vida_pikachu:
                        print("Perdiste! Bulbasaur te ganó!")
                        exit()

                if object_in_cell == charizard:
                    os.system("cls")
                    from random import randint
                    import os

                    VIDA_INICIAL_PIKACHU = 65
                    VIDA_INICIAL_CHARIZARD = 76

                    vida_pikachu = VIDA_INICIAL_PIKACHU
                    vida_charizard = VIDA_INICIAL_CHARIZARD

                    while vida_pikachu > 0 and vida_charizard > 0:
                        # Se turnan para pelear

                        # turno de charizard
                        print("Turno de charizard")
                        ataque_charizard = randint(1, 2)
                        if ataque_charizard == 1:
                            print("Charizard ataca con Envite Ígneo")
                            vida_pikachu -= 12
                        else:
                            print("Charizard ataca con Puño Fuego")
                            vida_pikachu -= 8

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        elif vida_charizard < 0:
                            vida_charizard = 0

                        barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                                    " " * (100 - barra_de_vida_pikachu),
                                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_de_vida_charizard = int(vida_charizard * 100 / VIDA_INICIAL_CHARIZARD)
                        print("Charizard:    [{}{}] [{}/{}]".format("*" * barra_de_vida_charizard,
                                                                     " " * (100 - barra_de_vida_charizard),
                                                                     vida_charizard, VIDA_INICIAL_CHARIZARD))

                        input("Enter para continuar...\n")

                        if vida_pikachu == 0:
                            break
                        elif vida_charizard == 0:
                            break

                        # Turno de Pikachu
                        print("Turno de Pikachu")
                        ataque_pikachu = None
                        while ataque_pikachu not in ["B", "O", "N"]:
                            ataque_pikachu = input(
                                "¿Que ataque deseas hacer? [B] Bola Voltio, [O] Onda Trueno, [N]Nada: ")
                        os.system("cls")
                        if ataque_pikachu == "B":
                            print("Pikachu ataca con Bola Voltio")
                            vida_charizard -= 10
                        elif ataque_pikachu == "O":
                            print("Pikachu ataca con Onda Trueno")
                            vida_charizard -= 14
                        elif ataque_pikachu == "N":
                            print("Pikachu no hace nada")
                            vida_charizard = vida_charizard

                        if vida_pikachu < 0:
                            vida_pikachu = 0
                        elif vida_charizard < 0:
                            vida_charizard = 0

                        barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
                        print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                                    " " * (100 - barra_de_vida_pikachu),
                                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

                        barra_de_vida_charizard = int(vida_charizard * 100 / VIDA_INICIAL_CHARIZARD)
                        print("Charizard:    [{}{}] [{}/{}]".format("*" * barra_de_vida_charizard,
                                                                     " " * (100 - barra_de_vida_charizard),
                                                                     vida_charizard, VIDA_INICIAL_CHARIZARD))
                        input("Enter para continuar... \n")

                    if vida_pikachu > vida_charizard:
                        print("Ganaste! Completaste el juego!!")
                        exit()
                    elif vida_charizard > vida_pikachu:
                        print("Perdiste! Charizard te ganó.")
                        exit()

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "--"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("|" + "-" * (MAP_WIDTH * 2) + "|")

    # Movimiento
    direction = readchar.readchar()

    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        break

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position





