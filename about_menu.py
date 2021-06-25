"""The about menu for the game.

Written by: Dick Loveland
"""
from renderer import Renderer
from inputs import Inputs


class AboutMenu:
    """Draws the about menu for the game"""

    renderer = Renderer.get_instance()
    inputs = Inputs.get_instance()

    def __init__(self):
        self.text1 = ("Credits: ",
                      {'x': 50, 'y': 10},
                      'basic',
                      Renderer.WHITE)
        self.text2 = ("Max Clark",
                      {'x': 50, 'y': 30},
                      'basic',
                      Renderer.WHITE)
        self.text3 = ("Nathan Holst",
                      {'x': 50, 'y': 40},
                      'basic',
                      Renderer.WHITE)
        self.text4 = ("Dick Loveland",
                      {'x': 50, 'y': 50},
                      'basic',
                      Renderer.WHITE)
        self.next_action = ''

    def update(self, inputs: dict, options):
        """Performs the world update for the about menu

        Args:
            inputs ([type]): [description]
            options ([type]): [description]

        Returns:
            [type]: [description]
        """
        if(len(inputs['keys']) != 0):
            if(inputs['keys'][0] == 'back'):
                self.next_action = 'pop'
        return options

    def render(self):
        AboutMenu.renderer.draw_text(
            self.text1[0], self.text1[1], self.text1[2], self.text1[3])
        AboutMenu.renderer.draw_text(
            self.text2[0], self.text2[1], self.text2[2], self.text2[3])
        AboutMenu.renderer.draw_text(
            self.text3[0], self.text3[1], self.text3[2], self.text3[3])
        AboutMenu.renderer.draw_text(
            self.text4[0], self.text4[1], self.text4[2], self.text4[3])

    def get_next_action(self):
        return self.next_action
