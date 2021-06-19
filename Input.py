import copy
import pygame
from pygame.locals import *

defalts = {
	"up"		= K_w,
	"down"	= K_s,
	"left"	= K_a,
	"right"	= K_d
}

class Input:
	def __init__(self):
		this.map = default
		this.currentInputs = {}
		this.keys = []
		this.mouse = {}

	def set_inputs(self, location, key); 
		this.map[location] = key

	def get_keys(self):
	for event in pygame.event.get():
		if ( event.type == KEYDOWN ):
			if ( event.key == self.map["up"] ):
				this.keys.append('up')
			elif ( event.key == self.map["down"] ):
				this.keys.append('down')
			elif ( event.key == self.map["left"] ):
				this.keys.append('left')
			elif ( event.key == self.map["right"] ):
				this.keys.append('right')
			elif ( event.key == K_ESCAPE ):
				this.keys.append('back')
			elif ( event.key == K_RETURN ):
				this.keys.append('enter')

	def get_mouse(self):
	pass

	def get(self):
		this.get_mouse()
		this.get_keys()

		return {
			"mouse": this.mouse,
			"keys": this.keys 
		}
