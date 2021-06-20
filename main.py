# Game main By Dick Loveland

import random, pygame, sys, math, time
import Menu, Game
from pygame.locals import *



import Helper
Helper.startAll()

from Renderer import Renderer
from Input import Input


GAMECAPTION = 'Group 9: Final Project'

FPS = 30
renderList = []

def main():

	pygame.display.set_caption(GAMECAPTION)

	while True:
		#menuOptions = Menu.start()
		menuOptions = {
			'guards': 1
		}
		Game.start(menuOptions)

if __name__ == '__main__':
    main()
