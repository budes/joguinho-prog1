def move_character(coords, side, can_move, step=2, mod=2):
    """
    Take cares of the movement:
    u -> Up | d -> Down | r -> Right | l -> Left

    The mod value is to take care of the fact that the line height is
    greater than the line width.
    """
    if can_move:
        if side in "lr":
            coords[1] += step * mod if side == "r" else -step * mod
        elif side in "ud":
            coords[0] += step if side == "d" else -step


def dash(coords, side, step=2, mod=2):
    """
    In order to not be that complex of a function, it just uses
    the default movement function with a modifier to the step value.
    """

    move_character(coords, side, step*mod)

def attack_animation(scr, character_coordinates, side, symbol="#", distance=3, width=1):
    """
    The system of side will be the same as the movement parts
    It will use the symbol to emulate the attack pattern

    There is the need of pointing out the scr to the function because
    it will handle the drawing directly
    """

    scr.addstr(1, 1, "funciona")
    # In order to make it simple -> It will try to draw everything
    # until it gets an exception, then it will try the next one and ignore
    # this one that failed

    if side in "lr":
        for y in range(-width, width+1):
            for x in range(1, distance+1):
                if side == "r":
                    try: scr.addch(character_coordinates[0] + y, character_coordinates[1] + x, symbol)
                    except: ...
                else:
                    try: scr.addch(character_coordinates[0] + y, character_coordinates[1] - x, symbol)
                    except: ...

    elif side in "ud":
        for y in range(1, distance):
            for x in range(-width, width + 1):
                if side == "u":
                    try: scr.addch(character_coordinates[0] - y, character_coordinates[1] + x, symbol)
                    except: pass
                else:
                    try: scr.addch(character_coordinates[0] + y, character_coordinates[1] + x, symbol)
                    except: pass
