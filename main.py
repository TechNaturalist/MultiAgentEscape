# Game main By Dick Loveland

import random, pygame, sys, math, time
import Menu

from pygame.locals import *
from Renderer import Renderer
from Input import Input

GAMECAPTION = 'Group 9: Final Project'

FPS = 30
renderList = []

def main():
	pygame.init()
	pygame.display.set_caption(GAMECAPTION)

	while True:
		menuOptions = Menu.start()
		#Game.start(menuOptions)

if __name__ == '__main__':
    main()
