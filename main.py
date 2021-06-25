# Game main By Dick Loveland

import pygame
import helper
import game
import menu


helper.start_all()

GAMECAPTION = 'Group 9: Final Project'
FPS = 30
render_list = []


def main():
    pygame.display.set_caption(GAMECAPTION)

    while True:
      
        menu_options = menu.start()
        game.start(menu_options)

        #gold = 0
        #for i in range(5):
        #    gold += game.start(menu_options, i)
        print(f"The Thief was able to steal a total of {gold} gold!")
        print("Thank you for playing!")

if __name__ == '__main__':
    main()
