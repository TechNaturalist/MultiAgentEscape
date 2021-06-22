from player_agent import PlayerAgent
from guard_agent import GuardAgent
import tile
import pygame
from pygame.locals import *
from Input import Input
from Renderer import Renderer

render_list = []
board = []
guards = []
walls = []
player = None

BOARD_WIDTH = 20


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
    global guards, board, player, walls

    walls = [(10, 10)]
    guards = [GuardAgent((11, 11))]
    player = PlayerAgent((12, 12))

    board = tile.create_board(BOARD_WIDTH, walls, guards, player)


def update(inputs):
    global render_list
    render_list = []

    # for guard in guards:
    #     guard.getSight(get_percepts(guard))
    #     render_list.append(guard.update())

    return False


def render():
    RENDERER.game_background()
    for sprite in render_list:
        sprite.render()

    RENDERER.draw_grid()
    RENDERER.finish_rendering()


def get_percepts(sprite):
    percepts = []

    percepts.append(board[sprite.position['x']][sprite.position['y']])
    # Adjacent Tiles
    try:
        percepts.append(board[sprite.position['x'] - 1]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass

    try:
        percepts.append(board[sprite.position['x'] - 1]
                        [sprite.position['y']])
    except IndexError:
        pass

    try:
        percepts.append(board[sprite.position['x'] - 1]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x']]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 0]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 1]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 1]
                        [sprite.position['y'] - 0])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 1]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass

    # Non adjecent tiles
    try:
        percepts.append(board[sprite.position['x'] - 2]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 2]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 2]
                        [sprite.position['y'] - 0])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 2]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 2]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 2]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 1]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 1]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 0]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] - 0]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 1]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 1]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 2]
                        [sprite.position['y'] - 2])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 2]
                        [sprite.position['y'] - 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 2]
                        [sprite.position['y'] - 0])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 2]
                        [sprite.position['y'] + 1])
    except IndexError:
        pass
    try:
        percepts.append(board[sprite.position['x'] + 2]
                        [sprite.position['y'] + 2])
    except IndexError:
        pass

    return percepts
