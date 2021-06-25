"""An abstract class for agents. Provides base functionality
for all agents.

Written by: Dick Loveand, Nathan Holst
"""
import pygame
import helper
from game import Game
from menu import Menu


helper.start_all()

GAMECAPTION = 'Group 9: Final Project'
FPS = 30
render_list = []


def main():
    pygame.display.set_caption(GAMECAPTION)

    while True:
        menu = Menu()
        menu_options = menu.start()
        gold = 0

        if menu_options['map'] == 5:
            for i in range(5):
                menu_options['map'] = i
                game = Game()
                gold += game.start(menu_options)
        else:
            game = Game()
            gold += game.start(menu_options)

        print(f"The Thief was able to steal a total of {gold} gold!")
        print("Thank you for playing!")


if __name__ == '__main__':
    main()
