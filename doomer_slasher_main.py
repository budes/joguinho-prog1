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

    FPS = 60
    scr.nodelay(True)
    curses.curs_set(0)

    max_width = curses.COLS
    max_height = curses.LINES

    character = "█"
    character_step = 4
    character_mod = 2
    dash_multiplier = 3

    boss = "▒"
    boss_step = 1
    boss_mod = 2
    boss_buffer = 2

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
    terminate = False
    # main loop
    while not terminate:
        # frame rate setup
        time.sleep(1/FPS)

        try:
            key = scr.getkey()
            active_keys.add(key)
        except: key = ""

        if 'KEY_UP' in active_keys:
            if " " in active_keys and can_move(max_height, char_coords[0], -character_step * dash_multiplier): dash(char_coords, "u", character_step, dash_multiplier)
            elif can_move(max_height, char_coords[0], -character_step): move_character(char_coords, "u", character_step, character_mod)
        if 'KEY_DOWN' in active_keys:
            if " " in active_keys and can_move(max_height, char_coords[0], character_step * dash_multiplier): dash(char_coords, "d", character_step, dash_multiplier)
            elif can_move(max_height, char_coords[0], character_step): move_character(char_coords, "d", character_step, character_mod)
        if 'KEY_LEFT' in active_keys:
            if " " in active_keys and can_move(max_width, char_coords[1], -character_step * character_mod * 2): dash(char_coords, "l", character_step, dash_multiplier)
            elif can_move(max_width, char_coords[1], -character_step * character_mod): move_character(char_coords, "l", character_step, character_mod)
        if 'KEY_RIGHT' in active_keys:
            if " " in active_keys and can_move(max_width, char_coords[1], character_step * character_mod * 2): dash(char_coords, "r", character_step, dash_multiplier)
            elif can_move(max_width, char_coords[1], character_step * character_mod): move_character(char_coords, "r", character_step, character_mod)

        if key == 'q':  # quit the loop if 'q' is pressed
            terminate = True

        scr.clear()

        # Boss_movement update and if it had touched any wall
        directions, side_inversion = boss_movement(boss_coords, max_width, max_height, directions)

        # Updates the current attacks
        for index in range(len(attacks)-1, -1, -1):
            move = attacks[index]
            if move[0] == "side" and move[2] not in [-1, None]:
                attacks[index][2] = side_attack(scr, char_coords, move[1], max_width, max_height, move[2])
            elif move[2] == -1:
                terminate = True
                break
            else:
                attacks.pop(index)

        # If it notices any wall touching, it will tell the side it inverted at
        # And use it in the side attack function
        if side_inversion:
            if side_inversion in "lu": curr_pos = 2
            elif side_inversion == "r": curr_pos = max_width - 3
            else: curr_pos = max_height - 3

            attacks.append(["side", side_inversion, side_attack(scr, char_coords, side_inversion, max_width, max_height, curr_pos)])


        scr.addstr(10, 10, str(active_keys))
        scr.addch(*boss_coords, boss)
        scr.border(0)
        game_map(scr, obstacles, borders)
        scr.addch(*char_coords, character)

        if " " in active_keys and key in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
            count_not_active_buffer = 0
            active_keys.clear()
        elif " " in active_keys and not key in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
            count_not_active_buffer += 1
            if count_not_active_buffer > FPS//2: active_keys.clear()
        else:
            active_keys.clear()

curses.wrapper(main)
