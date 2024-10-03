import random 

def generate_obstacles(y, x):
    cords = []
    for i in range(10):
        cords.append(((random.randint(1, y-2)), (random.randint(0, int(x * 0.4)))))
        cords.append(((random.randint(1, y-2)), (random.randint(int(x * 0.6), x-1))))
    return cords

def game_map(scr, cords, borders):
    i = 0
    for cord in cords:
        scr.addch(*cord, borders[i])
        i += 1
        if i > 7: i = 0

def can_move(limit, cord, n):
    if not limit > cord + n >= 0:
        return False
    return True