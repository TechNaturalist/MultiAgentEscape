import pygame
from pygame.locals import *
from Renderer import Renderer
from Input import Input
from MainMenu import MainMenu

#Syntactic Sugar
FIRST = 0

#
INPUT = Input.getInstance()
RENDERER = Renderer.getInstance()
#
menuStack = [ MainMenu() ]
inputs  = {}
last = 0;
Options = {}

def start():
	global inputs
	while ( len(menuStack) != 0 ):
		inputs = INPUT.getInput()
		update()
		render();

	return Options;


def update():
	global Options
	Options = menuStack[last].update( inputs, Options );
	nextInstruction( menuStack[last].nextAction() )

def render():
	RENDERER.menuBackground();
	menuStack[last].render();
	RENDERER.finishRendering();
	pass

def nextInstruction( action ):
	if   ( action == 'back' ):
		menuStack.pop()
		last -= 1
	elif ( action == 'addOption'):
		menuStack.append( OptionsMenu() )
		last += 1
	elif ( action == 'addAbout'):
		menuStack.append( AboutMenu() )
		last += 1
	else:
		pass
