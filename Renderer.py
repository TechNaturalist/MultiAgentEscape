import pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 640
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
BGCOLOR		= (  0,   0,   0)


class Renderer:

	__instance = None
	def getInstance():
		if Renderer.__instance == None:
			Renderer()
    
	def __init__(self):
		self.display = pygame.display.set_mode( ( HEIGHT, WIDTH ) )

    def drawSprite(self, imagePath, coords):
        try:
            x = coords['x'] * CELLSIZE
            y = coords['y'] * cellsize
            image = pygame.image.load(imagePath)
            image = pygame.transform.smoothscale(image, ( self.cellsize, self.cellsize ))
            self.display.blit( image, (x,y) )
        except:
            pass

    def drawGrid(self):
        for x in range(0, self.windowWidth, self.cellsize):
            pygame.draw.line(self.display, DARKGRAY, (x, 0), (x, self.windowHeight))
        for y in range(0, self.windowHeight, self.cellsize):
            pygame.draw.line(self.display, DARKGRAY, (0, y), (self.windowWidth, y))

    def drawScore(self, score):
        scoreSurf = self.basicFont.render('Score: %s' % (score), True, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (self.windowWidth - 120, 10)
        self.display.blit(scoreSurf, scoreRect)
