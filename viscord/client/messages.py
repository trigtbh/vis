import uuid
import blessed
term = blessed.Terminal()
import colors
import cursor
import keyshortcuts
import requests
import config
import registry
import sys

import socket

global s
s = None

global data
data = {}

global typed_message
typed_message = ""

def draw_typed_message():
    print(term.move(int(term.width * 0.1 + 1), int(term.height * 0.9) - 1) + term.on_color_rgb(*hex_to_rgb(colors.field)) + term.color_rgb(*hex_to_rgb(colors.text)) + typed_message + " " * (int(term.width * 0.8 - 1)))



def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

def draw_background():
    print(term.home + term.clear, end=" ")
    for y in range(term.height):
        print(term.move(y, 0) + term.on_color_rgb(*hex_to_rgb(colors.background)) + ' ' * term.width, end="")


def draw_menu():
    tlx = int(term.width * 0.1)
    tly = int(term.height * 0.1)

    for y in range(tly, tly + int(term.height * 0.8)):
        print(term.move(y, tlx) + term.on_color_rgb(*hex_to_rgb(colors.div)) + ' ' * int(term.width * 0.8), end="")

def show_recent_messages():
    ...


def redraw_all():
    draw_background()
    draw_menu()

    draw_typed_message()

    print("")



def main(user_token, server_id, channel_id):
    global s, data
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.connect((config.HOST, config.SOCKET_PORT))
    s.send(user_token.encode())


    resp = requests.post(f"{config.API_URL}/api/messages/get_recent", json={
        "server_id": server_id,
        "channel_id": channel_id,
        "user_token": user_token
    })
    if resp.status_code != 200:
        return
    data = resp.json()["data"]



    redraw_all()
    with term.cbreak():
        val = ""
        while True:
            sx = term.width
            sy = term.height
            val = term.inkey(timeout=0.01)
            if not val:
                if term.width != sx or term.height != sy:
                    redraw_all()
                continue
            if val.code == term.KEY_ESCAPE:
                s.close()
                break
            