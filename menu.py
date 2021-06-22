import pygame
from pygame.locals import *
from renderer import Renderer
from input import Input
from main_menu import MainMenu

# Syntactic Sugar
FIRST = 0

#
INPUT = Input.get_instance()
RENDERER = Renderer.get_instance()
#
menu_stack = [MainMenu()]
inputs = {}
last = 0
Options = {}


def start():
    global inputs
    while (len(menu_stack) != 0):
        inputs = INPUT.get_input()
        update()
        render()

    return Options


def update():
    global Options
    Options = menu_stack[last].update(inputs, Options)
    next_instruction(menu_stack[last].next_action())


def render():
    RENDERER.menu_background()
    menu_stack[last].render()
    RENDERER.finish_rendering()
    pass


def next_instruction(action):
    if (action == 'back'):
        menu_stack.pop()
        last -= 1
    elif (action == 'addOption'):
        menu_stack.append(OptionsMenu())
        last += 1
    elif (action == 'addAbout'):
        menu_stack.append(AboutMenu())
        last += 1
    else:
        pass
