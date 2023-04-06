
import speech_recognition as sr
import pyttsx3
import re


def iniciar_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 130)
    engine.setProperty("voice", "spanish")
    return engine


def reconocer_voz(r):
    with sr.Microphone() as source:
        print("Podes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
    return text


def identificar_nombre(text):
    name = None
    patterns = ["me llamo ([a-zA-Z]+)", "mi nombre es ([a-zA-Z]+)", "^([a-zA-Z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)
            return name
        except IndexError:
            pass
    return name


def repetir_preg(parar, name, engine, r):
    if name:
        engine.say("Un gusto conocerte {}".format(name))
        return False
    else:
        engine.say("La verdad que no te entiendo, podrias repetirlo?")
        engine.runAndWait()
        text_again = reconocer_voz(r)
        name_again = identificar_nombre(text_again)
        if name_again:
            engine.say("Un gusto conocerte {}".format(name_again))
        else:
            repetir_preg(parar, name_again, engine, r)


def main():
    engine = iniciar_engine()
    engine.say("Hola, como te llamas?")
    engine.runAndWait()
    r = sr.Recognizer()
    text = reconocer_voz(r)
    name = identificar_nombre(text)
    parar = True
    while parar:
        parar = repetir_preg(parar, name, engine, r)
    print("Salio bien")
    engine.runAndWait()


if __name__ == "__main__":
    main()