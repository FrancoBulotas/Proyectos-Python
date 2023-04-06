
def pikachu_vs_bulbasaur(pikachu = 0, bulbasaur = 1):
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
        print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                    " " * (100 - barra_de_vida_pikachu),
                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

        barra_de_vida_bulbasaur = int(vida_bulbasaur * 100 / VIDA_INICIAL_BULBASAUR)
        print("Bulbasaur:     [{}{}] [{}/{}]".format("*" * barra_de_vida_bulbasaur,
                                                    " " * (100 - barra_de_vida_bulbasaur),
                                                    vida_bulbasaur, VIDA_INICIAL_BULBASAUR))

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
        print("Pikachu:      [{}{}] [{}/{}]".format("*" * barra_de_vida_pikachu,
                                                    " " * (100 - barra_de_vida_pikachu),
                                                    vida_pikachu, VIDA_INICIAL_PIKACHU))

        barra_de_vida_bulbasaur = int(vida_bulbasaur * 100 / VIDA_INICIAL_BULBASAUR)
        print("Bulbasaur:     [{}{}] [{}/{}]".format("*" * barra_de_vida_bulbasaur,
                                                    " " * (100 - barra_de_vida_bulbasaur),
                                                    vida_bulbasaur, VIDA_INICIAL_BULBASAUR))
        input("Enter para continuar... \n\n")

    if vida_pikachu > vida_bulbasaur:
        return 0
    if vida_bulbasaur > vida_pikachu:
        return 1
