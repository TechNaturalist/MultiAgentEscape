import pygame
from pygame.locals import *
from renderer import Renderer
from inputs import Inputs
from main_menu import MainMenu
from about_menu import AboutMenu

#
INPUT = Inputs.get_instance()
RENDERER = Renderer.get_instance()
#
menu_stack = [MainMenu()]
inputs = {}
last = 0
options = {}


def start():
    global inputs, menu_stack, options
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
    menu_stack[last].render()
    RENDERER.finish_rendering()


def next_instruction(action):
    global last, menu_stack
    if (action == 'pop'):
        menu_stack.pop()
        #menu_stack = menu_stack[:-1]
        last = last - 1
    elif (action == 'addOption'):
        menu_stack.append(OptionsMenu())
        last += 1
    elif (action == 'addAbout'):
        menu_stack.append(AboutMenu())
        last += 1
    else:
        pass
    return menu_stack
