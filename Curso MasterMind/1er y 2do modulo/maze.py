import os
import readchar
import random

obstacle_definition = """\
##########################
             #############
#########          #######
##############     #######
########        ##########
############     #########
#########       ##########
###########        #######
#######          #########
############      ########
##########   ##   ########
#############      #######
############   ###   #####
################        ##
##########            ####\
"""


POS_X = 0
POS_Y = 1
NUM_OF_MAP_OBJECTS = 6

my_position = [1, 1]
tail_lenght = 0
tail = []
map_objects = []

# Creando obstaculo en el mapa
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main Loop
while True:
    os.system("cls")
    # Genera objetos random en el mapa
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # Crea mapa y Personaje
    print("-" + "-" * (MAP_WIDTH * 2) + "-")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " +"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                if my_position[POS_X] == tail_piece[POS_X] and my_position[POS_Y] == tail_piece[POS_Y]:
                    print("Perdiste!!")
                    exit()

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("-" + "-" * (MAP_WIDTH * 3) + "-")

    # Movimiento
    direction = readchar.readchar()

    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

       # tail.insert(0, my_position.copy()) # Agrega un objeto a la lista de la cola
       # tail = tail[0:tail_lenght] # La cola va del 0 al tamaño de la cola
       # my_position[POS_Y] -= 1
       # my_position[POS_Y] %= MAP_HEIGHT # Para atravesar la pared y aparecer en el otro lado
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
            tail.insert(0, my_position.copy())
            tail = tail[0:tail_lenght]
            my_position = new_position



