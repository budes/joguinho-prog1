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
    curses.curs_set(0)

    max_width = curses.COLS
    max_height = curses.LINES

    character = "█"

    # coordinates system is based in y, x -> curses.addch(y, x)
    char_coords = [max_height//2, max_width//2]

    scr.addch(*char_coords, character)
    scr.refresh()

    active_keys = set()
    count_not_active_buffer = 0

    # main loop
    while True:
        # frame rate setup
        time.sleep(1/30)

        try:
            key = scr.getkey()
            active_keys.add(key)
        except: key = ""

        if 'KEY_UP' in active_keys:
            if " " in active_keys: dash(char_coords, "u")
            else: move_character(char_coords, "u")
        if 'KEY_DOWN' in active_keys:
            if " " in active_keys: dash(char_coords, "d")
            else: move_character(char_coords, "d")
        if 'KEY_LEFT' in active_keys:
            if " " in active_keys: dash(char_coords, "l")
            else: move_character(char_coords, "l")
        if 'KEY_RIGHT' in active_keys:
            if " " in active_keys: dash(char_coords, "r")
            else: move_character(char_coords, "r")

        if key == 'q':  # quit the loop if 'q' is pressed
            break

        scr.clear()
        scr.addch(*char_coords, character)
        scr.addstr(10, 10, str(list(active_keys)))

        if key != " " and key not in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
            # This countdown makes the input easier to put
            # The downside is that it makes the step longer
            count_not_active_buffer += 1

            if count_not_active_buffer == 2:
                count_not_active_buffer = 0
                active_keys.clear()

curses.wrapper(main)
