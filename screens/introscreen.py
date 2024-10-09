import curses
import time

arrows = ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]
wasd = ["w", "s", "a", "d"]

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

    # Selected button
    selected_button = 0

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # Selected
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) # Not selected


    # Creates the buttons, stores them by name and by index
    for index, button in enumerate(buttons.keys()):
        buttons[button].append(index)
        buttons[button].append(curses.newwin(button_height, button_width, start_y + index * button_height, start_x))


    terminate_game = False
    while not terminate_game:

        for line in range(len(intro_text)):
            scr.addstr(line + 2, max_width // 2 - len(intro_text[-1]) // 2 - 1, intro_text[line])

        scr.refresh()

        # Updates buttons
        for button in buttons.items():
            button[1][1].addstr(button_height//2, (button_width - len(button[0].upper())) // 2, button[0].upper())
            button[1][1].box()

            if button[1][0] == selected_button:
                button[1][1].bkgd(' ', curses.color_pair(1))
            else:
                button[1][1].bkgd(' ', curses.color_pair(2))

            button[1][1].refresh()

        try:
            key = scr.getkey()
        except:
            key = "Nothing"

        if key == "\n":
            for button in buttons.items():
                if button[1][0] == selected_button:
                    if button[0] == "start": return 1
                    if button[0] == "quit": return 0

        if key in (arrows[1], arrows[3], wasd[1], wasd[3]):
            selected_button += 1
            if selected_button == len(buttons):
                selected_button = 0

        elif key in (arrows[0], arrows[2], wasd[0], wasd[2]):
            selected_button -= 1
            if selected_button < 0:
                selected_button = len(buttons) - 1

