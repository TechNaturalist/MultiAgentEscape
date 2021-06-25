import pygame
from pygame.locals import *
from renderer import Renderer
from inputs import Inputs
from main_menu import MainMenu
from about_menu import AboutMenu
from options_menu import OptionsMenu
from help_menu import HelpMenu
#
INPUT = Inputs.get_instance()
RENDERER = Renderer.get_instance()
#
menu_stack = [MainMenu()]
inputs = {}
last = 0

options = {
    'map': 0,
    'player': 0
}


def start():
    global inputs, menu_stack, options, last
    menu_stack = [MainMenu()]
    last = 0
    while (len(menu_stack) != 0):
        inputs = INPUT.get_input()
        update()
        render()

    return options


def update():
    global options, menu_stack
    options = menu_stack[last].update(inputs, options)
    nex = menu_stack[last].get_next_action()
    menu_stack = next_instruction(nex)

def render():
    global menu_stack, last
    RENDERER.menu_background()
    if(len(menu_stack) != 0):
        menu_stack[last].render()
    RENDERER.finish_rendering()


def next_instruction(action):
    global last, menu_stack
    if (action == 'pop'):
        menu_stack.pop()
        last = last - 1
    elif (action == 'addOption'):
        menu_stack.append(OptionsMenu())
        last += 1
    elif (action == 'addHelp'):
        menu_stack.append(HelpMenu())
        last += 1

    elif (action == 'addAbout'):
        menu_stack.append(AboutMenu())
        last += 1
    else:
        pass
    return menu_stack
