def move_character(coords, side, dist):
    """
    Take cares of the movement:
    u -> Up | d -> Down | r -> Right | l -> Left

    The mod value is to take care of the fact that the line height is
    greater than the line width.
    """
    if side in "lr":
        coords[1] += dist
    elif side in "ud":
        coords[0] += dist


def dash(coords, side, dist):
    """
    In order to not be that complex of a function, it just uses
    the default movement function with a modifier to the step value.
    """
    move_character(coords, side, dist)

def can_move(limit, coord, n):
    if not limit > coord + n >= 0:
        return False
    return True

def get_max_dist(coords, side, normal_dist, obstacles, limit):
    max_dist = normal_dist

    while side == "d" and coords[0] + max_dist > limit -2:
        max_dist -= 1
    while side == "u" and coords[0] + max_dist < 1:
        max_dist += 1
    while side == "r" and coords[1] + max_dist > limit -2:
        max_dist -= 1
    while side == "l" and coords[1] + max_dist < 1:
        max_dist += 1

    for obs in obstacles:
        if side in "lr" and coords[0] == obs[0]:
            while side == "r" and coords[1] < obs[1] and coords[1] + max_dist >= obs[1]:
                max_dist -= 1
            while side == "l" and coords[1] > obs[1] and coords[1] + max_dist <= obs[1]:
                max_dist += 1
        elif side in "ud" and coords[1] == obs[1]:
            while side == "d" and coords[0] < obs[0] and coords[0] + max_dist >= obs[0]:
                max_dist -= 1
            while side == "u" and coords[0] > obs[0] and coords[0] + max_dist <= obs[0]:
                max_dist += 1
        if max_dist == 0: return 0

    return max_dist