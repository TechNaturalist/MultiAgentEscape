
# Game main By Dick Loveland

from Input import Input
from Renderer import Renderer
import random
import pygame
import sys
import math
import time
import Menu
import Game
from pygame.locals import *
import Helper
Helper.start_all()


GAMECAPTION = 'Group 9: Final Project'

FPS = 30
render_list = []


def main():
    pygame.display.set_caption(GAMECAPTION)

    while True:
        #menuOptions = Menu.start()
        menu_options = {
            'guards': 1
        }
        Game.start(menu_options)


if __name__ == '__main__':
    main()
