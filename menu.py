import pygame
from pygame.locals import *
from renderer import Renderer
from inputs import Inputs
from main_menu import MainMenu
from about_menu import AboutMenu
from options_menu import OptionsMenu
from help_menu import HelpMenu

class Menu :

    INPUT = Inputs.get_instance()
    RENDERER = Renderer.get_instance()
    def __init__(self): 
        self.menu_stack = [MainMenu()]
        self.last = 0
        self.inputs = {}
        self.options = {
    'map': 0,
    'player': 0
}

    def start(self):
        while (len(self.menu_stack) != 0):
            self.inputs = Menu.INPUT.get_input()
            self.update()
            self.render()

        return self.options


    def update(self):
        self.options = self.menu_stack[self.last].update(self.inputs, self.options)
        nex = self.menu_stack[self.last].get_next_action()
        self.next_instruction(nex)

    def render(self):
        Menu.RENDERER.menu_background()
        if(len(self.menu_stack) != 0):
            self.menu_stack[self.last].render()
        Menu.RENDERER.finish_rendering()

    def next_instruction(self, action):
        if (action == 'pop'):
            self.menu_stack.pop()
            self.last = self.last - 1
        elif (action == 'addOption'):
            self.menu_stack.append(OptionsMenu())
            self.last += 1
        elif (action == 'addHelp'):
            self.menu_stack.append(HelpMenu())
            self.last += 1

        elif (action == 'addAbout'):
            self.menu_stack.append(AboutMenu())
            self.last += 1
        else:
            pass
