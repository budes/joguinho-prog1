def move_character(coords, side, step=2, mod=2):
    if side in "lr":
        coords[1] += step * mod if side == "r" else -step * mod
    elif side in "ud":
        coords[0] += step if side == "d" else -step
