
def pikachu_vs_charizard(pikachu = 0, charizard = 1):
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
            vida_pikachu -= 13
        else:
            print("Charizard ataca con Puño Fuego")
            vida_pikachu -= 9

        if vida_pikachu < 0:
            vida_pikachu = 0
        elif vida_charizard < 0:
            vida_charizard = 0

        barra_de_vida_pikachu = int(vida_pikachu * 100 / VIDA_INICIAL_PIKACHU)
        print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                    " " * (100 - barra_de_vida_pikachu),
                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

        barra_de_vida_charizard = int(vida_charizard * 100 / VIDA_INICIAL_CHARIZARD)
        print("Charizard:     [{}{}] [{}/{}]".format("*" * barra_de_vida_charizard,
                                                    " " * (100 - barra_de_vida_charizard),
                                                    vida_charizard, VIDA_INICIAL_CHARIZARD))

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
        print("Charizard:     [{}{}] [{}/{}]".format("*" * barra_de_vida_charizard,
                                                    " " * (100 - barra_de_vida_charizard),
                                                    vida_charizard, VIDA_INICIAL_CHARIZARD))
        input("Enter para continuar... \n\n")

    if vida_pikachu > vida_charizard:
        return 0
    if vida_charizard > vida_pikachu:
        return 1
