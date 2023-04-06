import pytube
import PySimpleGUI as sg


sg.theme('DarkRed1')   # Agrega color a la ventana

#Todo lo que va a estar en la ventana tiene que estar en el layout
layout = [[sg.Text('Ingresar URL del video', key="0", size=(18, 2), font="TimesNewRoman")], [sg.InputText(size=(80, 4), font="TimesNewRoman")],
          [sg.Text("", size=(12, 1))],
          [sg.Button('Descargar', key='-Ok-', font="TimesNewRoman"), sg.Button("Cancelar", key="-Cancelar-", font="TimesNewRoman")]]

# Crea la ventana
window = sg.Window('Descargar videos de YouTube', layout)

# Bucle que procesa los "events" y obtiene los "values" de los inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-Cancelar-': # Si el usuario toca Cancelar o cierra la ventana
        break
    
    if event == "-Ok-":
        # Avisa que el archivo se descargo
        window.Element("-Ok-").Update(text="Tu video se descargó")
        # Donde se baja el video (en este caso el directorio desde el que se ejecuta el archivo)
        download_col = "./"
        # Obtiene el URL ingresado en la ventana de PySimpleGui
        video_url = values[0]
        # Crea la instancia del video de YouTube
        video_instance = pytube.YouTube(video_url)

        stream = video_instance.streams.get_highest_resolution()
        # Descarga el video
        stream.download()


window.close()
