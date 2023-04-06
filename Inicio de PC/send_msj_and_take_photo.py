import cv2
import time
import getpass
import os
from pushbullet import PushBullet


def send_text_and_file(save, access_token):
    TITLE = "IMAGEN INTRUSO"
    FILE = "user.png"

    text = "PRENDIERON TU PC"

    photo_taked = True
    num_cameras = 0

    # Envio de mensaje
    pb = PushBullet(access_token)
    push_text = pb.push_note("ALERTA", text)

    time.sleep(1)

    while photo_taked:
        try:
            # Elige la camara y saca foto
            camera = cv2.VideoCapture(num_cameras, cv2.CAP_DSHOW)

            time.sleep(1)

            # Lee la foto sacada
            return_value, image = camera.read()
            # Escribe en el disco la foto
            cv2.imwrite(os.path.join(save, FILE), image)
            # Elimina la sesion de la camara
            del camera

            photo_taked = False
        except Exception:
            num_cameras += 1
            time.sleep(5)

    time.sleep(1)

    # Envia el archivo
    with open(save + "\\" + FILE, "rb") as pic:
        file_data = pb.upload_file(pic, FILE)
    file_data["title"] = TITLE
    push_file = pb.push_file(**file_data)
    # Borra el .png
    os.remove(save + "\\" + FILE)


def main():
    time.sleep(30)

    getUser = getpass.getuser()
    save = 'C:\\Users\\' + getUser + "\\PycharmProjects\\PrimerPrograma\\Inicio de PC"

    access_token = 'o.NnReSMrcQgk0s0WdrRLDWNvZpqWn7bAt'

    send_text_and_file(save, access_token)


if __name__ == '__main__':
    main()







