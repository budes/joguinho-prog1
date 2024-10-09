# Mesmo que usando classes esse código ficaria mil vezes melhor de ler e de trabalhar, vou
# me limitar ao que foi ensinado nas aulas de prog1 da ufcg

import sys

sys.path.insert(1, "./scripts/")
sys.path.insert(1, "./screens/")

from character import *
from boss import *
from movement import *
from map import *
from buffs import *

from main import *
from introscreen import *

import curses
import time

if __name__ == "__main__":
    while True:
        value = curses.wrapper(introscreen)
        if value == 1:
            curses.wrapper(main)
        else:
            break
