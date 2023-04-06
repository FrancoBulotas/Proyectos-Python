
from requests_html import HTMLSession
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def bot_compra_gamer(session, url):
    while True:
        response = session.get(url)
        page_html = response.html.find('title')
        if len(page_html) > 0:
            print("Hay stock!!")
            driver = webdriver.Firefox()
            driver.get(url)
            sleep(2)
            driver.find_element(By.CLASS_NAME, "medio_desk").click()
            sleep(2)
            driver.find_element(By.CLASS_NAME, "badge-button").click()
            break
        else:
            print("No hay stock!!")
        sleep(30)


if __name__ == '__main__':
    url = "https://compragamer.com/producto/Disco_Solido_SSD_Team_256GB_GX2_530MB_s_10110"
    session = HTMLSession()

    bot_compra_gamer(session, url)
