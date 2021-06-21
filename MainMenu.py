from Renderer import Renderer
from Input import Input
import Helper

Renderer = Renderer.get_instance()
Input = Input.get_instance()

STATEMACHINE = ['play', 'options', 'help', 'about']


## Helper Class for organization ##

class MainMenuItem:
    def __init__(self, text, center, size, highlighted):
        self.text = text
        self.center = center
        self.size = size
        self.highlighted = highlighted

    def render(self):
        if not self.highlighted:
            Renderer.draw_text(self.text, self.center, 'menu', Renderer.WHITE)
        else:
            Renderer.draw_text(self.text, self.center, 'menu', Renderer.GREEN)


## Main Class ##

class MainMenu:
    def __init__(self):
        self.items = [
            MainMenuItem('Play', {'x': 75, 'y': 60}, 18, True),
            MainMenuItem('Options', {'x': 75, 'y': 65}, 18, False),
            MainMenuItem('Help', {'x': 75, 'y': 70}, 18, False),
            MainMenuItem('About', {'x': 75, 'y': 75}, 18, False)
        ]
        self.titleSize = "30"
        self.title = "Prison Escape"
        self.state = 'play'
        self.next_action = ''
        self.stateIndex = 0

    def update(self, inputs, options):
        if (len(inputs['keys']) != 0):
            if (inputs['keys'][0] == 'enter'):
                self.enter()
            elif (inputs['keys'][0] == 'back'):
                Helper.terminate()
            else:
                self.change_state(inputs)
        return options

    def enter(self):
        if (self.state == 'play'):
            self.next_action = 'pop'
        elif (self.state == 'options'):
            self.next_action = 'addOption'
        elif (self.state == 'help'):
            self.next_action = 'addHelp'
        elif (self.state == 'about'):
            self.next_action = 'addAbout'

    def get_next_action(self):
        return self.next_action

    def change_state(self, inputs):
        if (inputs['keys'] == 'up'):
            self.items[self.stateIndex].highlighted = False
            self.stateIndex = (self.stateIndex + 3) % 4
            self.state = STATEMACHINE[self.stateIndex]
            self.items[self.stateIndex].highlighted = True
        elif (inputs['keys'] == 'down'):
            self.items[self.stateIndex].highlighted = False
            self.stateIndex = (self.stateIndex + 1) % 4
            self.state = STATEMACHINE[self.stateIndex]
            self.items[self.stateIndex].highlighted = True
        else:
            pass

    def render(self):
        Renderer.draw_text(
            self.title, {'x': 50, 'y': 20}, 'title', Renderer.YELLOW)
        for item in self.items:
            item.render()
