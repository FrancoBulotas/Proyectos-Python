
import PySimpleGUI as sg


button_size = (10, 5)
PLAYER1 = "X"
PLAYER2 = "O"

current_player = PLAYER1

deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

layout = [[
              sg.Button("", key="0", size=button_size),
              sg.Button("", key="1", size=button_size),
              sg.Button("", key="2", size=button_size)
          ],
          [
              sg.Button("", key="3", size=button_size),
              sg.Button("", key="4", size=button_size),
              sg.Button("", key="5", size=button_size)
          ],
          [
              sg.Button("", key="6", size=button_size),
              sg.Button("", key="7", size=button_size),
              sg.Button("", key="8", size=button_size)
          ],
          [sg.Text("", key="-WINNER-")],
          [sg.Button("TERMINE", key="-OK-"), sg.Text("", size=(8, 3)), sg.Button(" JUGAR DE NUEVO", key="-PLAY-AGAIN-")]]

window = sg.Window("Demo Ta Te Ti", layout)
game_end = False


def clean_board():
    window.Element("0").Update(text="")
    window.Element("1").Update(text="")
    window.Element("2").Update(text="")
    window.Element("3").Update(text="")
    window.Element("4").Update(text="")
    window.Element("5").Update(text="")
    window.Element("6").Update(text="")
    window.Element("7").Update(text="")
    window.Element("8").Update(text="")
    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
    return deck


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-OK-":
        break

    if event == "-PLAY-AGAIN-" and game_end:
        deck = clean_board()
        game_end = False

    if event == "-PLAY-AGAIN-":
        deck = clean_board()

    if window.Element(event).ButtonText == "" and not game_end:
        deck[int(event)] = current_player
        window.Element(event).Update(text=current_player)

        for winner_play in winner_plays:
            if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
                game_end = True
                window.Element("-WINNER-").Update("Jugador " + current_player + " Ganó")

        if 0 not in deck:
            window.Element("-WINNER-").Update("El juego terminó, ninguno ganó")
            game_end = False

        if current_player == PLAYER1:
            current_player = PLAYER2
        else:
            current_player = PLAYER1

window.close()