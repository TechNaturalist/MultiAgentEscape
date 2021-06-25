from renderer import Renderer
from inputs import Inputs

class HelpMenu:

    renderer = Renderer.get_instance()
    inputs = Inputs.get_instance()

    def __init__(self):
        self.text1 = ("Welcome to the Prison Escape Game!: ", 
                      {'x': 30,'y': 10 }, 
                      'basic', 
                      HelpMenu.renderer.WHITE)
        self.text2 = ("To play use the W, A, S, D keys to move", 
                      {'x': 10,'y': 30 }, 
                      'basic', 
                      HelpMenu.renderer.WHITE)
        self.text3 = ("They will move you up, left, down, right, respectively", 
                      {'x': 10,'y': 33 }, 
                      'basic', 
                      HelpMenu.renderer.WHITE)
        self.text4 = ("You can change whether you play or the ai plays in the options", 
                      {'x': 10,'y': 40 }, 
                      'basic', 
                      HelpMenu.renderer.WHITE)
        self.next_action = ''

    def update(self, inputs, options):
        if(len(inputs['keys']) != 0):
            if(inputs['keys'][0] == 'back' or inputs['keys'][0] == 'enter'):
                self.next_action = 'pop'
        return options

    def render(self):
        HelpMenu.renderer.draw_text(self.text1[0], self.text1[1], self.text1[2], self.text1[3])
        HelpMenu.renderer.draw_text(self.text2[0], self.text2[1], self.text2[2], self.text2[3])
        HelpMenu.renderer.draw_text(self.text3[0], self.text3[1], self.text3[2], self.text3[3])
        HelpMenu.renderer.draw_text(self.text4[0], self.text4[1], self.text4[2], self.text4[3])
    def get_next_action(self):
        return self.next_action
