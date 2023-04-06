import random
from pprint import pprint
from pokeload import get_pokemon, get_all_pokemons


def get_player_profile(pokemon_list):
    return {
        "player_name": input("Cual es tu nombre: \n"),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def fight(player_profile, enemy_pokemon):
    player_pick_name = []

    print("El Pokemon enemigo es: {}\n".format(enemy_pokemon["name"]))

    for name in player_profile["pokemon_inventory"]:
        player_pick_name.append(name["name"])
    player_pick = input("Elige uno de los siguiente pokemos para atacar {}".format(player_pick_name))

    if player_pick == player_pick_name[0]:
        print("Vas a atacar con {}".format(player_pick_name[0]))
    if player_pick == player_pick_name[1]:
        print("Vas a atacar con {}".format(player_pick_name[1]))
    if player_pick == player_pick_name[2]:
        print("Vas a atacar con {}".format(player_pick_name[2]))


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    pprint(player_profile)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)


if __name__ == "__main__":
    main()
