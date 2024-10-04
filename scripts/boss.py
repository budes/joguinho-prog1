from random import randint
import curses

from movement import *

def boss_movement(boss_coords, max_x, max_y, directions, step=1):
    """
    Basically makes the boss move in the predicted pattern -> Bouncing
    The movement is simple in order to make it easier to play and to build
    this game.

    - directions [x, y]
        - x = 0 -> Left, x = 1 -> Right
        - y = 0 -> Down, y = 1 -> Up

        If it's value is -1, -1 it will set a random value instead
    - boss_coords work the same as the coordinate system from curses
    [y, x], which means that, while we check directions as [x, y] we
    would do the inverse to those coordinates.

    - max_x = the most it can go to the right
    - max_y = the most it can go down

    - step = the pace it takes, it's the basics from the movement part
    """

    #directions[0] = x | directions[1] = y

    # The main idea about this variable is: If it is inverted, it will return the side it will need to work with
    inversion = False

    if directions == [-1, -1]: directions = [randint(0,1), randint(0,1)]

    # X inversion
    if (directions[0] and boss_coords[1] + step >= max_x -1) or (not directions[0] and boss_coords[1] - step <= 0):
        inversion = "l" if directions[0] == 0 else "r"
        directions[0] = int(directions[0] != 1)

    # Y inversion
    if (not directions[1] and boss_coords[0] + step >= max_y) or (directions[1] and boss_coords[0] - step <= 0):
        inversion = "d" if directions[1] == 0 else "u"
        directions[1] = int(directions[1] != 1)

    move_character(boss_coords, "l" if directions[0] == 0 else "r", step)
    move_character(boss_coords, "d" if directions[1] == 0 else "u", step)

    return directions, inversion

def side_attack(scr, character, side, max_x, max_y, curr_pos, trace="#"):
    """
    - scr is for two reasons, first, it will draw something in the screen,
    and to detect if something (the character) is in there.

    - side is about the side it touched, it will create a wall that go to
    the oposite side, which means: if i touch the left wall, side = l and
    the attack will go to the right

    - curr_pos is based on the axis we're dealing with.
        - so, if you are dealing with the x axis (left or right), curr_pos will be the check in that direction

    """

    if side in "lr":
        for y in range(max_y):
            if scr.inch(y, curr_pos) == character: return -1
            scr.addch(y, curr_pos, trace)

        if max_x - 2 > curr_pos and curr_pos > 1:
            if side == "r": curr_pos -= 1
            else: curr_pos += 1

        else: return None

    elif side in "ud":
        for x in range(max_x):
            if scr.inch(curr_pos, x) == character: return -1
            scr.addch(curr_pos, x, trace)

        if max_y - 2 > curr_pos and curr_pos > 1:
            if side == "d": curr_pos -= 1
            else: curr_pos += 1

        else: return None

    return curr_pos
