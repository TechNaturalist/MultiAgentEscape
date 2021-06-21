from Renderer import Renderer
from Input import Input
import Helper

Renderer = Renderer.getInstance()
Input = Input.getInstance()

STATEMACHINE = ['play','options', 'help', 'about']


## Helper Class for organization ##

class mainMenuItem:
	def __init__( self, text, center, size, highlighted  ):
		self.text = text
		self.center = center
		self.size = size
		self.highlighted = highlighted

	def render(self):
		if  not self.highlighted :
			Renderer.drawText(self.text, self.center, 'menu', Renderer.WHITE) 
		else:
			Renderer.drawText(self.text, self.center, 'menu', Renderer.GREEN)


## Main Class ##

class MainMenu:
	def __init__(self):
		self.items = [
			mainMenuItem('Play',	{'x': 75, 'y':60}, 18, True),
			mainMenuItem('Options',	{'x': 75, 'y':65}, 18, False),
			mainMenuItem('Help',	{'x': 75, 'y':70}, 18, False),
			mainMenuItem('About',	{'x': 75, 'y':75}, 18, False)
		]
		self.titleSize = "30"
		self.title = "Prison Escape"
		self.state = 'play'
		self.nextAct = ''
		self.stateIndex = 0

	def update(self, inputs, options  ):
		if (len(inputs['keys']) != 0  ):
			if ( inputs['keys'][0] == 'enter' ):
				self.enter()
			elif ( inputs['keys'][0] == 'back' ):
				Helper.terminate()
			else:
				self.changeState(inputs)
		return options

	def enter(self):
		if ( state == 'play'):
			self.nextAction = 'pop'
		elif (state == 'options'):
			self.nextAction = 'addOption'
		elif (state == 'help'):
			self.nextAction = 'addHelp'
		elif ( state == 'about'):
			self.nextAction = 'addAbout'


	def nextAction(self):
		return self.nextAct;

	def changeState(self, inputs):
		if ( inputs['keys'] == 'up') :
			self.items[self.stateIndex].highlighted = False
			self.stateIndex = ( self.stateIndex + 3 ) % 4 
			self.state = STATEMACHINE[ self.stateIndex  ]
			self.items[self.stateIndex].highlighted = True
		elif ( inputs['keys'] == 'down' ):
			self.items[self.stateIndex].highlighted = False
			self.stateIndex = ( self.stateIndex + 1 ) % 4 
			self.state = STATEMACHINE[ self.stateIndex  ]
			self.items[self.stateIndex].highlighted = True
		else:
			pass


	def render(self):
		Renderer.drawText(self.title, {'x': 50, 'y':20}, 'title', Renderer.YELLOW  )
		for item in self.items:
			item.render() 
