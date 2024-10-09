import random 
import curses

def generate_obstacles(y, x):
    cords = []
    for i in range(10):
        cords.append([(random.randint(4, y-2)), (random.randint(0, int(x * 0.4)))])
        cords.append([(random.randint(4, y-2)), (random.randint(int(x * 0.6), x-1))])
    return cords

def game_map(scr, cords, borders):
    i = 0
    for cord in cords:
        scr.addch(*cord, borders[i])
        i += 1
        if i > 7: i = 0

def game_area(scr, x, y):
    scr.addstr(3, 1, "▀" * (x-2))
    scr.addstr(y-1, 1, "▄" * (x-2))
    
    scr.addch(3, 0, "▛")
    scr.addch(3, x-1, "▜")
    scr.addch(y-1, 0, "▙")

    for i in range(4, y-1):
        scr.addch(i, 0, "▌")
        scr.addch(i, x-1, "▐")