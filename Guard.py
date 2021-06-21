from Renderer import Renderer

class Guard:
	RENDERER = Renderer.getInstance()
	def __init__(self, debug, position):
		self.debug = debug
		self.position = position
		self.sight = []

	def update(self):
		return self

	def render(self):
		if self.debug:
			for tile in self.sight:
				Guard.RENDERER.colorTile( tile,  Guard.RENDERER.CORAL)
		Guard.RENDERER.drawGuard( self.position )

	def getSight(self, tiles):
		self.sight = tiles
