import pygame
from pygame.locals import *
from Input import Input
from Renderer import Renderer
from Guard import Guard

renderList = []
gameMap = []

def start(options):
	global RENDERER, INPUTS, inputs

	RENDERER = Renderer.getInstance()
	INPUTS = Input.getInstance()
	endGame = False
	inputs = {}

	gameInit( options )

	while not endGame:
		inputs = INPUTS.getInput();
		endGame = update( inputs )
		render()

def gameInit( options ):
	global guards, gameMap

	guards = []

	for i in range(options['guards']):
		guards.append( Guard( True, { 'x':4, 'y':4 } ) )

	gameMap = []
	## Creating a map (need to automate)
	for i in range(20):
		tmp = []
		for j in range(20):
			tmp.append( {'x': i, 'y': j} )
		gameMap.append(tmp)

def update(inputs):
	global renderList 
	renderList = []

	for guard in guards:
		guard.getSight( getPercepts( guard ) )
		renderList.append( guard.update() )

	return False

def render():
	RENDERER.gameBackground()
	for sprite in renderList:
		sprite.render()

	RENDERER.drawGrid()
	RENDERER.finishRendering()


def getPercepts( sprite ):
	percepts = []


	percepts.append(gameMap[sprite.position['x'] ][sprite.position['y']  ])
	## Adjacent Tiles
	try:
		percepts.append(gameMap[sprite.position['x'] -1][sprite.position['y'] -1 ])
	except IndexError:
		pass

	try:
		percepts.append(gameMap[sprite.position['x'] -1][sprite.position['y']])
	except IndexError:
		pass

	try:
		percepts.append(gameMap[sprite.position['x'] -1][sprite.position['y'] +1 ])
	except IndexError:
		pass
	try:
		percepts.append(gameMap[sprite.position['x'] ][sprite.position['y'] -1 ])
	except:
		pass
	try:
		percepts.append(gameMap[sprite.position['x'] -0][sprite.position['y'] +1 ])
	except:
		pass
	try:
		percepts.append(gameMap[sprite.position['x'] +1][sprite.position['y'] -1 ])
	except:
		pass
	try:
		percepts.append(gameMap[sprite.position['x'] +1][sprite.position['y'] -0 ])
	except:
		pass
	try:
		percepts.append(gameMap[sprite.position['x'] +1][sprite.position['y'] +1 ])
	except:
		pass

	#Non adjecent tiles
	try:
		percepts.append(gameMap[sprite.position['x'] -2][sprite.position['y'] -2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -2][sprite.position['y'] -1 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -2][sprite.position['y'] -0 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -2][sprite.position['y'] +1 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -2][sprite.position['y'] +2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -2][sprite.position['y'] -1 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -1][sprite.position['y'] -2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -1][sprite.position['y'] +2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -0][sprite.position['y'] -2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] -0][sprite.position['y'] +2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] +1][sprite.position['y'] -2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] +1][sprite.position['y'] +2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] +2][sprite.position['y'] -2 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] +2][sprite.position['y'] -1 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] +2][sprite.position['y'] -0 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] +2][sprite.position['y'] +1 ])
	except:
		pass 
	try:
		percepts.append(gameMap[sprite.position['x'] +2][sprite.position['y'] +2 ])
	except:
		pass

	return percepts
