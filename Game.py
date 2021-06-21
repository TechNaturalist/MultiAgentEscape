import pygame
from pygame.locals import *
from Input import Input
from Renderer import Renderer
from Guard import Guard

render_list = []
game_map = []


def start(options):
    global RENDERER, INPUTS, inputs

    RENDERER = Renderer.get_instance()
    INPUTS = Input.get_instance()
    game_map = False
    inputs = {}

    game_init(options)

    while not game_map:
        inputs = INPUTS.get_input()
        game_map = update(inputs)
        render()


def game_init(options):
    global guards, game_map

    guards = []

    for i in range(options['guards']):
        guards.append(Guard(True, {'x': 4, 'y': 4}))

    game_map = []
    # Creating a map (need to automate)
    for i in range(20):
        tmp = []
        for j in range(20):
            tmp.append({'x': i, 'y': j})
        game_map.append(tmp)


def update(inputs):
    global render_list
    render_list = []

    for guard in guards:
        guard.getSight(get_percepts(guard))
        render_list.append(guard.update())

    return False


def render():
    RENDERER.game_background()
    for sprite in render_list:
        sprite.render()

    RENDERER.draw_grid()
    RENDERER.finish_rendering()


def get_percepts(sprite):
    percepts = []

    percepts.append(game_map[sprite.position['x']][sprite.position['y']])
    # Adjacent Tiles
    try:
        percepts.append(game_map[sprite.position['x'] - 1]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass

    try:
        percepts.append(game_map[sprite.position['x'] - 1]
                        [sprite.position['y']])
    except IndexError:
        pass

    try:
        percepts.append(game_map[sprite.position['x'] - 1]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x']]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 0]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 1]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 1]
                        [sprite.position['y'] - 0])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 1]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass

    # Non adjecent tiles
    try:
        percepts.append(game_map[sprite.position['x'] - 2]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 2]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 2]
                        [sprite.position['y'] - 0])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 2]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 2]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 2]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 1]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 1]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 0]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] - 0]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 1]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 1]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 2]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 2]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 2]
                        [sprite.position['y'] - 0])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 2]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass
    try:
        percepts.append(game_map[sprite.position['x'] + 2]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass

    return percepts
