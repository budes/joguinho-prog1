import curses

def tutorial(scr):
    scr.clear()

    max_width = curses.COLS
    max_height = curses.LINES

    text = (
        "If you need/want to quit earlier, press 'q', it's the default 'quit' key.",
        "",
        "To move and attack, depending on what you chose on settings, use wasd or the arrows:",
        "   - The default is using wasd, so if you dont like it, change it in the settings;",
        "   - If you're using wasd to move, you attack using the arrows;",
        "   - If you're using the arrows to move, you attack using wasd.",
        "",
        "Dash extends your movement range, by a certain multiplier.",
        "In order to dash, press 'space' and then a movement key.",
        "Dash/move through an attack to dodge them.",
        "",
        "The boss has three lifes, you have 1, have a good use of it.",
        "",
        "Use the buffs available:",
        "   - The shield (🛡️), to defend you, automatically, of one attack;",
        "   - The extender (🏹), to extend your attack range;",
        "   - The blank (💥), to delete every attack on the screen (press 'b')."
    )

    while True:

        for count, text_part in enumerate(text):
            scr.addstr(10+count, max_width//4, text_part)

        scr.addstr(4*max_height//5, max_width//4, "To exit this window, learn the first line of the tutorial (press 'q')")

        scr.refresh()

        try: key = scr.getkey()
        except: key = "Nothing"

        if key == 'q': break
