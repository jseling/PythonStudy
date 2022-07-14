# hello_world.py
# https://www.youtube.com/watch?v=-_z2RPAH0Qk&ab_channel=RealPython

import PySimpleGUI as sg

layout = [
    [sg.Text("Hello from PySimpleGUI")],
    [sg.Button("OK")]
]

# create the window
window = sg.Window("Hello World", layout, margins=(200, 100))

# create an event loop
while True:
    event, values = window.read()
    # End program if user closes windows or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()    