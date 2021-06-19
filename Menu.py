import pygame
from pygame.locals import *
from Renderer import Renderer
from Input import Input

#Syntactic Sugar
FIRST = []


#
menuStack = []
inputs  = []


def start(screen):
	while len(menuStack != 0 ):
		inputs = Inputs.get()
		menuStack, options = update()
		render(screen);

	return options;


def update():


	pass

def render(screen):
	menuStack[FIRST].render();
	pass
