"""An abstract class for agents. Provides base functionality
for all agents.

Written by: Dick Loveand, Nathan Holst
"""
import pygame
import helper
import game


helper.start_all()

GAMECAPTION = 'Group 9: Final Project'
FPS = 30
render_list = []


def main():
    pygame.display.set_caption(GAMECAPTION)

    while True:
        # menu_options = menu.start()
        menu_options = {'guards': 3}
        gold = 0
        for i in range(5):
            gold += game.start(menu_options, i)
        print(f"The Thief was able to steal a total of {gold} gold!")
        print("Thank you for playing!")
        break


if __name__ == '__main__':
    main()
