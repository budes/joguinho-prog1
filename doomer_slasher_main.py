# Mesmo que usando classes esse código ficaria mil vezes melhor de ler e de trabalhar, vou
# me limitar ao que foi ensinado nas aulas de prog1 da ufcg

import sys
sys.path.insert(1, "./scripts/")

from character import *

import curses
import time

borders = ["▀", "▄", "▟", "▜", "▙", "▛", "▐", "▌"]


def main(scr):
    scr.clear()
    scr.nodelay(True)

    max_width = curses.COLS
    max_height = curses.LINES

    character = "█"
    # coordinates system is based in y, x -> curses.addch(y, x)
    char_coords = [max_height//2, max_width//2]

    scr.addch(*char_coords, character)
    scr.refresh()

    active_keys = set()

    # main loop
    while True:
        time.sleep(1/60)

        try:
            key = scr.getkey()
            active_keys.add(key)
        except: key = ""

        if 'KEY_UP' in active_keys:    move_character(char_coords, "u")
        if 'KEY_DOWN' in active_keys:  move_character(char_coords, "d")
        if 'KEY_LEFT' in active_keys:  move_character(char_coords, "l")
        if 'KEY_RIGHT' in active_keys: move_character(char_coords, "r")
        if key == 'q':  # quit the loop if 'q' is pressed
            break

        scr.clear()
        scr.addch(*char_coords, character)

        if key not in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
            active_keys.clear()


curses.wrapper(main)
