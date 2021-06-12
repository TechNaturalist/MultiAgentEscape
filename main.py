# Game main By Dick Loveland

import random, pygame, sys, math, time
from pygame.locals import *
from Renderer import Renderer

FPS = 5
WINDOWWIDTH = 640
WINDOWHEIGHT = 640
CELLSIZE = 128
RADIUS = math.floor(CELLSIZE/2.5)
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
GRAY      = (100,  100,100)
PURPLE    = (155,   0, 155)
YELLOW    = (255, 255,   0)
BGCOLOR = BLACK

UP = 'up'
LEFT = 'left'
RIGHT = 'right'
SHOOT = 'shoot'
GRAB = 'grab'
RELEASE = 'release'
DOWN = 'down'

theInput = ''

renderList = []

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, RENDERER

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	RENDERER = Renderer(DISPLAYSURF, CELLSIZE, WINDOWWIDTH, WINDOWHEIGHT, BASICFONT)

	pygame.display.set_caption('Wumpus World')

	showStartScreen()
	while True:
		runGame()
		showGameOverScreen()

def runGame():
	init_game()
	endGame = False
	while not endGame: # main game loop
		inputs()
		endGame = update()
		render()
		FPSCLOCK.tick(FPS)

def init_game():
	pass
def inputs():
	pass
def update():

for agent in agentlist:
	renderList.append(agent)

	pass   

def render():
	DISPLAYSURF.fill(BGCOLOR)
	RENDERER.drawGrid()

	for sprite in renderList:
		sprite.render()

	pygame.display.update()


def drawPressKeyMsg():
	pressKeySurf = BASICFONT.render('Press a key to play.', True, YELLOW)
	pressKeyRect = pressKeySurf.get_rect()
	pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
	DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
	if len(pygame.event.get(QUIT)) > 0:
		terminate()

	keyUpEvents = pygame.event.get(KEYUP)
	if len(keyUpEvents) == 0:
		return None

	if keyUpEvents[0].key == K_ESCAPE:
		terminate()

	return keyUpEvents[0].key


def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
