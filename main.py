# Game main By Dick Loveland

import pygame
import Helper
import Game

Helper.start_all()

GAMECAPTION = 'Group 9: Final Project'
FPS = 30
render_list = []


def main():
    pygame.display.set_caption(GAMECAPTION)

    while True:
        # menuOptions = Menu.start()
        menu_options = {'guards': 3}
        Game.start(menu_options)


if __name__ == '__main__':
    main()
