from pushbullet import PushBullet
from requests_html import HTMLSession
from time import sleep
from datetime import datetime


def current_date():
    now = datetime.now()

    year = str(now.year)
    month = now.month
    day = str(now.day)

    if month == 1:
        month = "ene"
    elif month == 2:
        month = "feb"
    elif month == 3:
        month = "mar"
    elif month == 4:
        month = "abr"
    elif month == 5:
        month = "may"
    elif month == 6:
        month = "jun"
    elif month == 7:
        month = "jul"
    elif month == 8:
        month = "agos"
    elif month == 9:
        month = "sep"
    elif month == 10:
        month = "oct"
    elif month == 11:
        month = "nov"
    elif month == 12:
        month = "dic"

    today_date_string = day + " " + month + " " + year

    return today_date_string


def bot_riot_bridge(session, url):
    while True:
        response = session.get(url)
        html_page = response.html.find('.gs-bidi-start-align')

        print(html_page)


def main():
    current_date()

    url = "https://www.perfil.com/buscador?q=corte+puente+pueyrredon#gsc.tab=0&gsc.q=corte%20puente%20pueyrredon&gsc.sort=date"
    session = HTMLSession()

    bot_riot_bridge(session, url)


if __name__ == '__main__':
    main()
