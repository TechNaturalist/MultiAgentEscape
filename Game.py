import pygame
from pygame.local import *
from Input import Input
from Renderer import Renderer



def start(options):
	global RENDERER, INPUTS, renderList, inputs

	RENDERER = Renderer.getInsance()
	INPUTS = Input.getInstance()
	renderList = []
	endGame = False
	inputs = {}

	gameInit()

	while not endgame
		inputs = INPUTS.getInput();
		endGame = update()
		render()

def gameInit( options ):
	global guards, players, 
	

def update(inputs):
	agent in agentlist:
		renderList.append(agent)
	pass

def render()
	RENDERER.gameBackground()
	RENDERER.drawGrid()
	for sprite in renderList:
		sprite.render()
	RENDERER.finishRendering()

