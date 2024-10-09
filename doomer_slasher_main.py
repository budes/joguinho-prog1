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

arrows = ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]
wasd = ["w", "s", "a", "d"]

movement_keys = wasd
attack_keys = arrows

def introscreen(scr):
    scr.clear()

    curses.curs_set(0)

    max_width = curses.COLS
    max_height = curses.LINES

    intro_text = (
    "   ░▒▓███████▓▒░   ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓██████████████▓▒░  ░▒▓████████▓▒░ ░▒▓███████▓▒░",
    "   ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░",
    "   ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░",
    "   ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓██████▓▒░   ░▒▓███████▓▒░",
    "   ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░",
    "   ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░",
    "   ░▒▓███████▓▒░   ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░",
    "",
    "  ░▒▓██████▓▒░ ░▒▓█▓▒░         ░▒▓██████▓▒░   ░▒▓███████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓███████▓▒░",
    " ░▒▓█▓▒░       ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░",
    " ░▒▓█▓▒░       ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░",
    "  ░▒▓█████▓▒░  ░▒▓█▓▒░        ░▒▓████████▓▒░  ░▒▓██████▓▒░  ░▒▓████████▓▒░ ░▒▓██████▓▒░   ░▒▓███████▓▒░",
    "       ░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░",
    "       ░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        ░▒▓█▓▒░░▒▓█▓▒░",
    "░▒▓███████▓▒░  ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓███████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░"
    )

    # Set the size and position for the button
    button_height, button_width = 3, 20
    start_y, start_x = max_height//2, max_width//2 - button_width//2  # Position of the button

    buttons = {"start": [], "settings": [], "quit": []}

    for index, button in enumerate(buttons.keys()):
        buttons[button].append(index)
        buttons[button].append(curses.newwin(button_height, button_width, start_y + index * button_height, start_x))

    while True:

        for line in range(len(intro_text)):
            scr.addstr(line + 2, max_width // 2 - len(intro_text[-1]) // 2 - 1, intro_text[line])

        # Set the size and position for the button
        button_height, button_width = 3, 20
        start_y, start_x = max_height//2, max_width//2 - button_width//2  # Position of the button

        scr.refresh()

        # Create a window for the button
        for button in buttons.items():
            button[1][1].addstr(button_height//2, (button_width - len(button[0].upper())) // 2, button[0].upper())
            button[1][1].box()
            button[1][1].refresh()

        try:
            key = scr.getkey()
        except: ...

        if key == "q": break


def main(scr):
    scr.clear()

    # the screen part
    FPS = 200
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

    attack_frames = 5
    character_attack = [0, attack_frames]
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    # definition of the boss properties
    boss = "█"
    boss_step = 1
    boss_mod = 2

    boss_buffer = 10
    boss_move_tick = boss_buffer # it is like that so it moves in the first cycle

    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    boss_max_life = 3
    boss_lives = 3

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

        # Movement
        if movement_keys[0] in active_keys:
            if " " in active_keys: dash(char_coords, "u", get_max_dist(char_coords, "u", -character_step * dash_multiplier, obstacles, max_height))
            else: move_character(char_coords, "u", get_max_dist(char_coords, "u", -character_step, obstacles, max_height))
        if movement_keys[1] in active_keys:
            if " " in active_keys: dash(char_coords, "d", get_max_dist(char_coords, "d", character_step * dash_multiplier, obstacles, max_height))
            else: move_character(char_coords, "d", get_max_dist(char_coords, "d", character_step, obstacles, max_height))
        if movement_keys[2] in active_keys:
            if " " in active_keys: dash(char_coords, "l", get_max_dist(char_coords, "l", -character_step * character_mod * dash_multiplier, obstacles, max_width))
            else: move_character(char_coords, "l", get_max_dist(char_coords, "l", -character_step * character_mod, obstacles, max_width))
        if movement_keys[3] in active_keys:
            if " " in active_keys: dash(char_coords, "r", get_max_dist(char_coords, "r", character_step * character_mod  * dash_multiplier, obstacles, max_width))
            else: move_character(char_coords, "r", get_max_dist(char_coords, "r", character_step * character_mod, obstacles, max_width))

        if 'q' in active_keys:  # quit the loop if 'q' is pressed
            terminate = True

        scr.clear()

        # This parts makes sure the attacks does not stop right away, so you have more than 1 frame to hit the boss
        if character_attack[1] < attack_frames:
            character_attack = sword_attack(scr, char_coords, boss_coords, character_attack[2], character_attack[1] + 1)

        # This part is to detect new inputs
        elif attack_keys[0] in active_keys:
            character_attack = sword_attack(scr, char_coords, boss_coords, "u", 0)
        elif attack_keys[2] in active_keys:
            character_attack = sword_attack(scr, char_coords, boss_coords, "l", 0)
        elif attack_keys[3] in active_keys:
            character_attack = sword_attack(scr, char_coords, boss_coords, "r", 0)
        elif attack_keys[1] in active_keys:
            character_attack = sword_attack(scr, char_coords, boss_coords, "d", 0)

        # CHECKS IF THE BOSS WAS HIT

        if character_attack[0] == 1:
            boss_lives -= 1
            character_attack = [0, attack_frames]

        if boss_lives == 0: terminate = True

        # Boss_movement update and if it had touched any wall
        if boss_move_tick >= boss_buffer:
            directions, side_inversion = boss_movement(boss_coords, max_width, max_height, directions, obstacles)
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

            attack_tick = 5 if side_inversion in "ud" else 2

            # attack = ["type_of_attack", info_about_attack]
            # in case of the side attack: ["side", "which side is it coming from", current_covered_position, current_tick, tick_of_actioni]
            # we plan to still add another type of attack, a time based one only
            attacks.append(["side", side_inversion, side_attack(scr, char_coords, side_inversion, max_width, max_height, curr_pos,), 0, attack_tick])

            # As it spends ticks in delay, it will not generate any more attacks
            side_inversion = None

        scr.addstr(10, 10, str(character_attack))

        scr.addch(*char_coords, character, curses.color_pair(1))
        scr.addch(*boss_coords, boss, curses.color_pair(2))

        game_map(scr, obstacles, borders)
        game_area(scr, max_width, max_height)

        life_bar(scr, boss_max_life, boss_lives, max_width)

        if " " in active_keys and not active_keys.isdisjoint(movement_keys):
            count_not_active_buffer = 0
            active_keys.clear()
        elif " " in active_keys and active_keys.isdisjoint(movement_keys):
            count_not_active_buffer += 1
            if count_not_active_buffer > FPS: active_keys.clear()
        else:
            active_keys.clear()

curses.wrapper(introscreen)
