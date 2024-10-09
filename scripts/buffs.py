import random

def show_buffs(scr, current_buffs, buffs):
    for i in range(len(current_buffs)):
        if current_buffs[i]:
            scr.addstr(1, (i+1) * 3, buffs[i])

def generate_buff(buff_on_map, x, y):
    if random.randint(1, 100) == 5:
        buff_on_map.append(((random.randint(4, y-2)), (random.randint(4, x-2))))
        buff_on_map.append(random.randint(0, 2))

def render_buff(scr, buff_on_map):
    if buff_on_map[1] == 0:
        scr.addstr(*buff_on_map[0], "🛡️")
    elif buff_on_map[1] == 1:
        scr.addstr(*buff_on_map[0], "🏹")
    elif buff_on_map[1] == 2:
        scr.addstr(*buff_on_map[0], "💥")

def check_got_buff(buff_on_map, current_buffs, player_coord):
    y, x = buff_on_map[0]
    if player_coord[0] in range(y-4, y+4) and player_coord[1] in range(x-4, x+4):
        buff_on_map.pop(0)
        current_buffs[buff_on_map.pop(0)] = True
    
