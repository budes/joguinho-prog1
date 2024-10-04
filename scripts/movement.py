def move_character(coords, side, step=1, mod=2):
    """
    Take cares of the movement:
    u -> Up | d -> Down | r -> Right | l -> Left

    The mod value is to take care of the fact that the line height is
    greater than the line width.
    """

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
