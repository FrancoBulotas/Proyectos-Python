
def pikachu_vs_squirtle(pikachu = 0, squirtle = 1):
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

        input("Enter para continuar...\n\n")

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
        input("Enter para continuar... \n\n")

    if vida_pikachu > vida_squirtle:
        return 0
    if vida_squirtle > vida_pikachu:
        return 1

    """ if pikachu_VS_squirtle.pikachu_vs_squirtle(0):
            squirtle = [100, 100]
            print("Le ganaste a Squirtle!")
        elif pikachu_VS_squirtle.pikachu_vs_squirtle(1):
            print("Perdiste! Squirtle te ganó")
            exit()"""
