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

    # the screen part
    FPS = 120
    scr.nodelay(True)
    curses.curs_set(0)

    # constants
    max_width = curses.COLS
    max_height = curses.LINES

    # definition of the characters properties
    character = "█"
    character_step = 4
    character_mod = 2
    dash_multiplier = 3
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # definition of the boss properties
    boss = "█"
    boss_step = 1
    boss_mod = 2

    boss_move_tick = 3 # starts with 3 so it moves
    boss_buffer = 3

    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # coordinates system is based in y, x -> curses.addch(y, x)
    char_coords = [max_height//2, max_width//2]
    boss_coords = [max_height//2 - 10, max_width//2]

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
            while True:
                key = scr.getkey()
                active_keys.add(key)
        except: key = ""

        if 'KEY_UP' in active_keys:
            if " " in active_keys: dash(char_coords, "u", get_max_dist(char_coords, "u", -character_step * dash_multiplier, obstacles, max_height))
            else: move_character(char_coords, "u", get_max_dist(char_coords, "u", -character_step, obstacles, max_height))
        if 'KEY_DOWN' in active_keys:
            if " " in active_keys: dash(char_coords, "d", get_max_dist(char_coords, "d", character_step * dash_multiplier, obstacles, max_height))
            else: move_character(char_coords, "d", get_max_dist(char_coords, "d", character_step, obstacles, max_height))
        if 'KEY_LEFT' in active_keys:
            if " " in active_keys: dash(char_coords, "l", get_max_dist(char_coords, "l", -character_step * character_mod * dash_multiplier, obstacles, max_width))
            else: move_character(char_coords, "l", get_max_dist(char_coords, "l", -character_step * character_mod, obstacles, max_width))
        if 'KEY_RIGHT' in active_keys:
            if " " in active_keys: dash(char_coords, "r", get_max_dist(char_coords, "r", character_step * character_mod  * dash_multiplier, obstacles, max_width))
            else: move_character(char_coords, "r", get_max_dist(char_coords, "r", character_step * character_mod, obstacles, max_width))

        if 'q' in active_keys:  # quit the loop if 'q' is pressed
            terminate = True

        scr.clear()

        # Boss_movement update and if it had touched any wall
        if boss_move_tick >= boss_buffer:
            directions, side_inversion = boss_movement(boss_coords, max_width, max_height, directions)
            boss_move_tick = 0
        else: boss_move_tick += 1

        # Updates the current attacks
        for index in range(len(attacks)-1, -1, -1):
            move = attacks[index]

            if move[0] == "side":
                if move[2] not in [-1, None]:
                    attack_feedback = side_attack(scr, char_coords, move[1], max_width, max_height, move[2])

                    if move[3] == move[4]:
                        attacks[index][2] = attack_feedback
                        attacks[index][3] = 0
                    else:
                        attacks[index][3] += 1

                elif move[2] == -1:
                    continue
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

            attack_tick = 4 if side_inversion in "ud" else 1

            # attack = ["type_of_attack", info_about_attack]
            # in case of the side attack: ["side", "which side is it coming from", current_covered_position, current_tick, tick_of_actioni]
            # we plan to still add another type of attack, a time based one only
            attacks.append(["side", side_inversion, side_attack(scr, char_coords, side_inversion, max_width, max_height, curr_pos,), 0, attack_tick])


        scr.addstr(10, 10, str(active_keys))

        scr.addch(*char_coords, character, curses.color_pair(1))
        scr.addch(*boss_coords, boss, curses.color_pair(2))

        scr.border(0)
        game_map(scr, obstacles, borders)

        if " " in active_keys and not active_keys.isdisjoint(["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]):
            count_not_active_buffer = 0
            active_keys.clear()
        elif " " in active_keys and active_keys.isdisjoint(["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]):
            count_not_active_buffer += 1
            if count_not_active_buffer > FPS: active_keys.clear()
        else:
            active_keys.clear()

curses.wrapper(main)
