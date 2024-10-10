def sword_attack(scr, character_coordinates, enemy_coordinates, side, attack_time, distance, boss_immunity, symbol="#", width=3):
    """
    The system of side will be the same as the movement parts
    It will use the symbol to emulate the attack pattern

    There is the need of pointing out the scr to the function because
    it will handle the drawing directly
    """

    # In order to make it simple -> It will try to draw everything
    # until it gets an exception, then it will try the next one and ignore
    # this one that failed

    side = str(side)

    if side in "lr":
        for y in range(-width, width+1):
            for x in range(1, distance+1):
                if side == "r":
                    try:
                        if not boss_immunity and [character_coordinates[0] + y, character_coordinates[1] + x] == enemy_coordinates: return [1, attack_time, side]
                        scr.addch(character_coordinates[0] + y, character_coordinates[1] + x, symbol)
                    except: ...
                else:
                    try:
                        if not boss_immunity and [character_coordinates[0] + y, character_coordinates[1] - x] == enemy_coordinates: return [1, attack_time, side]
                        scr.addch(character_coordinates[0] + y, character_coordinates[1] - x, symbol)
                    except: ...

    elif side in "ud":
        for y in range(1, distance):
            for x in range(-width, width + 1):
                if side == "u":
                    try:
                        if not boss_immunity and  [character_coordinates[0] - y, character_coordinates[1] + x] == enemy_coordinates: return [1, attack_time, side]
                        scr.addch(character_coordinates[0] - y, character_coordinates[1] + x, symbol)
                    except: pass
                else:
                    try:
                        if not boss_immunity and  [character_coordinates[0] + y, character_coordinates[1] + x] == enemy_coordinates: return [1, attack_time, side]
                        scr.addch(character_coordinates[0] + y, character_coordinates[1] + x, symbol)
                    except: pass

    return [0, attack_time, side]
