def can_move(limit, cord, n):
    if not limit > cord + n > 0:
        return False
    return True