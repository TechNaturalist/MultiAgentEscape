from renderer import Renderer
from inputs import Inputs

renderer = Renderer.get_instance()
inputs = Inputs.get_instance()


# Helper Class for organization #

class OptionsItem:
    def __init__(self, title, title_center ,options, center, size, highlighted):
        self.title = title
        self.title_center = title_center
        self.options = options
        self.state = 0
        self.center = center
        self.size = size
        self.highlighted = highlighted

    def next_item(self,instruct):
        if(instruct == 'right'):
            self.state = (self.state + len(self.options) + 1) % len(self.options)
        elif(instruct == 'left'):
            self.state = (self.state + len(self.options) - 1) % len(self.options)

    def render(self):
        if not self.highlighted:
            renderer.draw_text(self.title, self.title_center, 'menu', Renderer.WHITE)
            renderer.draw_text(self.options[self.state], self.center, 'menu', Renderer.WHITE)
        else:
            renderer.draw_text(self.title, self.title_center, 'menu', Renderer.WHITE)
            renderer.draw_text(self.options[self.state], self.center, 'menu', Renderer.GREEN)


# Main Class #

class OptionsMenu:
    def __init__(self):
        self.items = [
            OptionsItem('Maps',  {'x':25, 'y': 30},   ['Map1','Map2','Map3','Map4','Map5'],  {'x': 75, 'y': 30}, 18, True),
            OptionsItem('Player',  {'x':25, 'y': 40},   ['Agent - AI', 'Agent - Player'],  {'x': 75, 'y': 40}, 18, True),
        ]
        self.titleSize = "30"
        self.title = "Options"
        self.next_action = ''
        self.stateIndex = 0

    def update(self, inputs, options):

        self.set_options(options);

        if (len(inputs['keys']) != 0):
            if (inputs['keys'][0] == 'back' or inputs['keys'][0] == 'enter'):
                self.next_action = 'pop'
            else:
                self.change_state(inputs)

        new_options = {}
        new_options.update({'map': self.items[0].state})
        new_options.update({'player': self.items[1].state})

        return new_options

    def get_next_action(self):
        action = self.next_action
        self.next_action = ''
        return action

    def change_state(self, inputs):
        length = len(self.items)
        if (inputs['keys'][0] == 'up'):
            self.items[self.stateIndex].highlighted = False
            self.stateIndex = (self.stateIndex + length + 1) % length
            self.items[self.stateIndex].highlighted = True
        elif (inputs['keys'][0] == 'down'):
            self.items[self.stateIndex].highlighted = False
            self.stateIndex = (self.stateIndex + (length - 1)) % length
            self.items[self.stateIndex].highlighted = True
        else:
            self.items[self.stateIndex].next_item(inputs['keys'][0])

    def set_options(self, options):
        try:
            self.items[0].state = options['map']
        except:
            self.items[0].state = 0


    def render(self):
        renderer.draw_text(
            self.title,
            {'x': 40, 'y': 20},
            'title',
            Renderer.YELLOW)
        for item in self.items:
            item.render()
