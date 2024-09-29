import curses

def obstacle1(scr, y0, y1, x0, x1):
    scr.addstr(y0, x0, "▛")
    scr.addstr(y0, x1-1, "▜")
    scr.addstr(y1-1, x0, "▙")
    scr.addstr(y1-1, x1-1, "▟")
    scr.addstr(y0, x0 + 1, "▀" * (x1 - x0 -2))
    scr.addstr(y1-1, x0 + 1, "▄" * (x1 - x0 -2))
    for i in range(y0+1, y1-1):
        scr.addstr(i, x0, "▌")
        scr.addstr(i, x1-1, "▐")

def map1(scr, y, x):
    y // 6
    obstacle1(scr, y // 6, 2 * (y // 6), x // 8, 2 * (x // 8))
    obstacle1(scr, y // 6, 2 * (y // 6), x - (2 * (x // 8)), x - (x // 8))
    obstacle1(scr, y - (2 * (y // 6)), y - (y // 6), x // 8, 2 * (x // 8))
    obstacle1(scr, y - (2 * (y // 6)), y - (y // 6), x - (2 * (x // 8)), x - (x // 8))