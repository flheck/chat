import socket
import threading
import json


import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a little color to your windows


HEADER = 64
FORMAT = 'utf-8'
PORT = 12345
SERVER = "127.0.0.1"
DISCONNECT_MESSAGE = "!Disconnect"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"Connected to {client}")


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '  * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def createGui():
    layout_login_form = [[sg.Text('Name'), sg.Input(key='-IN-Name-')],
                            [sg.Text('Port'), sg.Input(key='-IN-Port-')],
                            [sg.Button('Submit')]]

    layout_login_frame = [[sg.Frame("Login", layout_login_form)]]
    
    # client = connectToSocket()

    send("Hello World!")
    message = client.recv(1024).decode(FORMAT)



    if message == "setNickname":
        win1 = sg.Window('Login', layout_login_frame)
    else:
        print("nothing")

    win2_active=False
    while True:
        ev1, vals1 = win1.Read(timeout=100)
        if ev1 == sg.WIN_CLOSED:
            client.send(DISCONNECT_MESSAGE.encode(FORMAT))
            break

        if ev1 == 'Submit'  and not win2_active:
            client.send(vals1["-IN-Name-"].encode(FORMAT))

            win2_active = True
            win1.Hide()
            layout2 =  [[sg.Text('Your output will go here', size=(40, 1))],
                [sg.Output(size=(110, 20), font=('Helvetica 10'))],
                [sg.Multiline(size=(70, 5), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('Send', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
                sg.Button('Exit', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

            win2 = sg.Window('Nimm-Spiel', layout2, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)
            while True:
                ev2, vals2 = win2.Read()
                if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                    win2.Close()
                    win2_active = False
                    win1.UnHide()
                    break

# def createGuiX():
#     layout = [[sg.Text('Your output will go here', size=(40, 1))],
#                 [sg.Output(size=(110, 20), font=('Helvetica 10'))],
#                 [sg.Multiline(size=(70, 5), enter_submits=False, key='-QUERY-', do_not_clear=False),
#                 sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
#                 sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

#     window = sg.Window('Nimm-Spiel', layout, font=('Helvetica', ' 13'), default_button_element_size=(8,2), use_default_focus=False)

#     while True:     # The Event Loop
#         event, value = window.read()
#         if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
#             break
#         if event == 'SEND':
#             send(value['-QUERY-'].rstrip())
#             input_user = value['-QUERY-'].rstrip()
#             print(input_user)
#             response_server = client.recv(1024).decode(FORMAT)
#             # EXECUTE YOUR COMMAND HERE
#             print('The command you entered was {}'.format(response_server), flush=True)

#     window.close()


# def createGui1():
#     layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Show'), sg.Button('Exit')]]

#     window = sg.Window('Nimm-Spiel', layout)

#     while True:  # Event Loop
#         event, values = window.read()
#         print(event, values)
#         send(values["-IN-"])
#         if event == sg.WIN_CLOSED or event == 'Exit':
#             break
#         if event == 'Show':
#             # Update the "output" text element to be the value of "input" element
#             window['-OUTPUT-'].update(values['-IN-'])

#     window.close()

# def createGui2():
#     # All the stuff inside your window. This is the PSG magic code compactor...
#     layout = [  [sg.Text(client.recv(1024).decode(FORMAT))],
#                 [sg.Text('Enter something on Row 2'), sg.InputText()],
#                 [sg.OK(), sg.Cancel()]]

#     # Create the Window
#     window = sg.Window('Nimm-Spiel', layout)
#     # Event Loop to process "events"
#     while True:             
#         event, values = window.read()
#         print(event, values)
#         send(values[0])
#         if event in (sg.WIN_CLOSED, 'Cancel'):
#             break

#     window.close()

# send("Hello world!")
createGui()