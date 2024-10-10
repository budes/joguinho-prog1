import time
import random 

def win(scr, x, y):

    scr.clear()

    victory_text = (
        "$$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\ $$$$$$\ $$\   $$\ $$\ ",
        "\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |\_$$  _|$$$\  $$ |$$ |",
        " \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |  $$ |  $$$$\ $$ |$$ |",
        "  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |  $$ |  $$ $$\$$ |$$ |",
        "   \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |  $$ |  $$ \$$$$ |\__|",
        "    $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |  $$ |  $$ |\$$$ |    ",
        "    $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ |$$$$$$\ $$ | \$$ |$$\ ",
        "    \__|     \______/  \______/       \__/     \__|\______|\__|  \__|\__|"
    )

    for i in range(20):
        scr.addstr(random.randint(1, y - 2), random.randint(1, x - 2), "☆")
        scr.addstr(random.randint(1, y - 2), random.randint(1, x - 2), "★")
        scr.addstr(random.randint(1, y - 2), random.randint(1, x - 2), "✧")
        scr.addstr(random.randint(1, y - 2), random.randint(1, x - 2), "✦")

    for line in range(len(victory_text)):
        scr.addstr(line + (y // 3) - (len(victory_text) // 2), x // 2 - len(victory_text[-1]) // 2 - 1, victory_text[line])

    scr.refresh()

    time.sleep(2)
