# Mesmo que usando classes esse código ficaria mil vezes melhor de ler e de trabalhar, vou
# me limitar ao que foi ensinado nas aulas de prog1 da ufcg

import curses

borders = ["▀", "▄", "▟", "▜", "▙", "▛", "▐", "▌"]


def main(scr):
    scr.clear()

    max_width = curses.COLS
    max_height = curses.LINES

    character = "█"
    # coordinates system is based in y, x -> curses.addch(y, x)
    char_coords = [max_height//2, max_width//2]

    scr.addch(*char_coords, character)
    scr.refresh()

    # main loop
    while True:
        key = scr.getkey()

        if key == 'KEY_UP':
            move_character(char_coords, "u")
        elif key == 'KEY_DOWN':
            move_character(char_coords, "d")
        elif key == 'KEY_LEFT':
            move_character(char_coords, "l")
        elif key == 'KEY_RIGHT':
            move_character(char_coords, "r")
        elif key == 'q':  # quit the loop if 'q' is pressed
            break

        scr.clear()
        scr.addch(*char_coords, character)

# Character handling
def move_character(coords, side):
    if side in "lr":
        coords[1] += 1 if side == "r" else -1
    elif side in "ud":
        coords[0] += 1 if side == "d" else -1

curses.wrapper(main)
