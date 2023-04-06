import pyautogui as pag
import random
import time

while True:
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    pag.moveTo(x, y, 0.5)
    time.sleep(2)