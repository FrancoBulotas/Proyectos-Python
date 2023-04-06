import random
from speak_and_listen import speak, hear_me
from requests_html import HTMLSession
from time import sleep

# from PIL import Image


"""def get_random_product_atributes_ml(session):
    url_ml = "https://www.mercadolibre.com.ar/ofertas#nav-header"
    main_site = session.get(url_ml)
    categories_ml = main_site.html.find(".promotion-item__description")
    category = random.choice(categories_ml)
    product_name = category.text.split("\n")[3]
    product_price = category.text.split("\n")[1]
    real_product_price = product_price.split(" ")[1]
    final_price = real_product_price.replace("$", "").replace("0,00", "0").replace("00,00", "00").replace(",00", "")
    return product_name, final_price
    """


def hear_price_and_get_numer():
    while True:
        try:
            price_user = hear_me()
            price_user = price_user.replace("$", "").replace(" + ", ".").replace(" más ", ".")\
                .replace(".000", ".").replace(" o ", ".").replace(",", ".")
            """.replace(",000", ".000").replace("000", ".000").replace("0")"""
            final_price_user = float(price_user)
            return final_price_user
        except ValueError:
            speak("No te entendi, podrias repetirlo?")


def get_random_product_atributes_fh(session, url_fh):
    main_site = session.get(url_fh)
    categories_fh = main_site.html.find(".product-list")
    category = random.choice(categories_fh)
    product_name = category.text.split("\n")[0]
    product_price = category.text.split("\n")[1]
    real_product_price = product_price.split(" ")[0]
    final_price = float(real_product_price.replace("$", "").replace("0,00", "0").replace("00,00", "00").replace(",00", ""))
    return product_name, final_price


def user_choose_category():
    urls = ["https://www.fullh4rd.com.ar/cat/124/nvidia/3", "https://www.fullh4rd.com.ar/cat/185/discos-ssd/1",
            "https://www.fullh4rd.com.ar/cat/390/amd-am5/1",
            "https://www.fullh4rd.com.ar/cat/supra/32/notebooks/1/mayor", "https://www.fullh4rd.com.ar/cat"]

    speak("Vamos a elegir una categoría para jugar, tienen 5 opciones: ")
    user_url = input("Pulsa el numero de la categoria que elijas\n1. Placas de video Nvidia\n2. Discos SSD"
                     "\n3. Microprocesadores AMD AM5\n4. Notebooks\n5. Variado\n")
    if user_url == "1": return urls[0]
    elif user_url == "2": return urls[1]
    elif user_url == "3": return urls[2]
    elif user_url == "4": return urls[3]
    elif user_url == "5": return urls[4]


def users_name():
    speak("Vamos a establecer los nombres de los jugadores")
    player1 = input("Jugador 1: ")
    player2 = input("Jugador 2: ")
    return player1, player2


def ask_users_amount(player):
    player_question = speak("{} cuanto pensás que vale?".format(player))
    return player_question


def players_guess(player1, player2):
    player1_question = ask_users_amount(player1)
    sleep(1)
    player1_guess = hear_price_and_get_numer()
    sleep(1)
    player2_question = ask_users_amount(player2)
    sleep(1)
    player2_guess = hear_price_and_get_numer()
    return player1_question, player1_guess, player2_question, player2_guess


def who_is_closer(player1, player2, player1_guess, player2_guess, final_price, scoreboard_player1, scoreboard_player2):
    speak("El precio final era {}".format(final_price))
    print(final_price)
    player1_final_number = player1_guess - final_price
    player2_final_number = player2_guess - final_price
    if player1_final_number < 0 or player2_final_number < 0:
        player1_final_number *= -1
        player2_final_number *= -1
    if player1_final_number > player2_final_number:
        speak("Esta ronda la ganó {}".format(player2))
        scoreboard_player2 += 1
    elif player2_final_number > player1_final_number:
        speak("Esta ronda la ganó {}".format(player1))
        scoreboard_player1 += 1
    else:
        speak("Fue un empate")
        scoreboard_player1 += 0
        scoreboard_player2 += 0
    return scoreboard_player1, scoreboard_player2


def main_game(session, player1, player2):
    scoreboard_player1 = 0
    scoreboard_player2 = 0
    for scoreboard in range(0, 1):
        url = user_choose_category()
        product_name, final_price = get_random_product_atributes_fh(session, url)
        speak("El nombre del producto es {}".format(product_name))
        print(product_name)
        player1_question, player1_guess, player2_question, player2_guess = players_guess(player1, player2)
        sleep(2)
        scoreboard_player1, scoreboard_player2 = who_is_closer(player1, player2, player1_guess, player2_guess,
                                                               final_price, scoreboard_player1, scoreboard_player2)
        print("{} va {}".format(player1, scoreboard_player1))
        print("{} va {}\n".format(player2, scoreboard_player2))
    return scoreboard_player1, scoreboard_player2


def final_winner(scoreboard_player1, scoreboard_player2, player1, player2):
    if scoreboard_player1 > scoreboard_player2:
        speak("El ganador es {}".format(player1))
    elif scoreboard_player2 > scoreboard_player1:
        speak("El ganador es {}".format(player2))
    else:
        speak("Empataron")


def main():
    session = HTMLSession()
    speak("Bienvenido al precio justo, vamos a ver quien sabe mas sobre el precio de los productos")
    player1, player2 = users_name()
    scoreboard_player1, scoreboard_player2 = main_game(session, player1, player2)
    final_winner(scoreboard_player1, scoreboard_player2, player1, player2)


if __name__ == "__main__":
    main()
