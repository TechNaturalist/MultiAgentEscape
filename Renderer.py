import pygame, math
from pygame.locals import *

WIDTH = 640
HEIGHT = 640
CELLSIZE = 128
RADIUS = math.floor(CELLSIZE/2.5)
assert WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WIDTH / CELLSIZE)
CELLHEIGHT = int(HEIGHT / CELLSIZE)


pygame.init()

class Renderer:

	__instance = None

	#				R    G    B
	WHITE		= (255, 255, 255)
	BLACK		= (  0,   0,   0)
	GREEN		= (  0, 255,   0)
	DARKGREEN	= (  0, 155,   0)
	DARKGRAY 	= ( 40,  40,  40)
	GRAY 		= (100,  100,100)
	PURPLE		= (155,   0, 155)
	YELLOW		= (255, 255,   0)
	BGCOLOR		= (  0,   0,   0)

	@staticmethod
	def getInstance():
		if Renderer.__instance == None:
			Renderer()
		return Renderer.__instance
    
	def __init__(self):
		if Renderer.__instance != None:
			raise Exception("This class is a singleton")
		else:
			self.display = pygame.display.set_mode( ( HEIGHT, WIDTH ) )
			self.MENUFONT	= pygame.font.Font('freesansbold.ttf', 24)
			self.TITLEFONT	= pygame.font.Font('freesansbold.ttf', 36)
			self.BASICFONT	= pygame.font.Font('freesansbold.ttf', 18)
			Renderer.__instance = self

	def drawText(self, text, center, font, color):
		if ( font == 'basic' ):
			surf = self.BASICFONT.render(text, True, color)
			rect = surf.get_rect()
			rect.topleft = (width(center['x']) - 9, height(center['y']) - 9)
		elif ( font == 'menu'):
			surf = self.MENUFONT.render(text, True, color)
			rect = surf.get_rect()
			rect.topleft = (width(center['x']) - 12, height(center['y']) - 12)
		elif ( font == 'title'):
			surf = self.TITLEFONT.render(text, True, color)
			rect = surf.get_rect()
			rect.topleft = (width(center['x']) - 18, height(center['y'])- 18)
		self.display.blit(surf, rect)

	def menuBackground(self):
		self.display.fill(self.BGCOLOR)

	def finishRendering(self):
		pygame.display.update()

def width(x):
	return int(WIDTH * x / 100)

def height(y):
	return int(HEIGHT *y / 100)
