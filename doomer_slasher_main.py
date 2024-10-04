# Mesmo que usando classes esse código ficaria mil vezes melhor de ler e de trabalhar, vou
# me limitar ao que foi ensinado nas aulas de prog1 da ufcg

import sys
sys.path.insert(1, "./scripts/")

from character import *
from boss import *
from movement import *
from map import *

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
    enemy = "▒"

    # coordinates system is based in y, x -> curses.addch(y, x)
    char_coords = [max_height//2, max_width//2]
    boss_coords = [max_height//2 - 10, max_width//2]

    scr.addch(*boss_coords, character)
    scr.addch(*char_coords, character)

    scr.refresh()

    directions = [-1, -1]
    active_keys = set()
    count_not_active_buffer = 0

    attacks = []
    obstacles = generate_obstacles(max_height, max_width)

    # main loop
    while True:
        # frame rate setup
        time.sleep(1/60)

        try:
            key = scr.getkey()
            active_keys.add(key)
        except: key = ""

        if 'KEY_UP' in active_keys:
            if " " in active_keys: dash(char_coords, "u")
            else: move_character(char_coords, "u", can_move(max_height, char_coords[0], -2))
        if 'KEY_DOWN' in active_keys:
            if " " in active_keys: dash(char_coords, "d")
            else: move_character(char_coords, "d", can_move(max_height, char_coords[0], 2))
        if 'KEY_LEFT' in active_keys:
            if " " in active_keys: dash(char_coords, "l")
            else: move_character(char_coords, "l", can_move(max_width, char_coords[1], -4))
        if 'KEY_RIGHT' in active_keys:
            if " " in active_keys: dash(char_coords, "r")
            else: move_character(char_coords, "r", can_move(max_width, char_coords[1], 4))

        if key == 'q':  # quit the loop if 'q' is pressed
            break

        scr.clear()

        # Boss_movement update and if it had touched any wall
        directions, side_inversion = boss_movement(boss_coords, max_width, max_height, directions)

        # Updates the current attacks
        for index in range(len(attacks)-1, -1, -1):
            move = attacks[index]
            if move[0] == "side" and move[2] not in [-1, None]:
                attacks[index][2] = side_attack(scr, character, move[1], max_width, max_height, move[2])
            else:
                attacks.pop(index)
        # If it notices any wall touching, it will tell the side it inverted at
        # And use it in the side attack function
        if side_inversion:
            if side_inversion in "lu": curr_pos = 2
            elif side_inversion == "r": curr_pos = max_width - 3
            else: curr_pos = max_height - 3

            attacks.append(["side", side_inversion, side_attack(scr, character, side_inversion, max_width, max_height, curr_pos)])


        scr.addstr(10, 10, str(attacks))
        scr.addch(*boss_coords, enemy)
        scr.border(0)
        game_map(scr, obstacles, borders)
        scr.addch(*char_coords, character)

        if key != " " and key not in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
            # This countdown makes the input easier to put
            # The downside is that it makes the step longer
            count_not_active_buffer += 1

            if count_not_active_buffer == 2:
                count_not_active_buffer = 0
                active_keys.clear()

curses.wrapper(main)
