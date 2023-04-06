
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'spanish')

r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def hear_me():
    with sr.Microphone() as source:
        print("Te escucho...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-ES")
            print("Entendi: {}".format(text))
            return text
        except Exception:
            return

