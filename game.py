from __future__ import annotations
from coalition import Coalition
from typing import Tuple, List
import copy
import pygame
from tile import Tile
from inputs import Inputs
from renderer import Renderer
from maps import Map1, Map2, Map3, Map4, Map5
from percept import see, hear
import a_star
import random

render_list = []
board = []
guards = []
walls = []
player = None
door = None
player_path = None
traveled = []

BOARD_WIDTH = 20

def start(options):
    global RENDERER, INPUTS, action

    RENDERER = Renderer.get_instance()
    INPUTS = Inputs.get_instance()
    game_map = False
    action = ''

    game_init(options)

    initiative = [player] + guards


    update(player, action)
    render()
    while not game_map:
        curr_agent = initiative.pop(0)
        if (type(player).__name__ == 'HumanAgent'
            and type(curr_agent).__name__ == 'HumanAgent'):
            action = block_parse_inputs(INPUTS.get_input())
        # Run agents turn.
        game_map = update(curr_agent, action)
        initiative.append(curr_agent)
        render()
    if player.gold == 0:
        print("The Thief was captured and the gold was returned.")
    else:
        print(f"The Thief escaped with {player.gold} gold!")
    return player.gold


def game_init(options):
    global guards, board, player, walls, door, player_path, traveled
    
    game_maps = [Map1, Map2, Map3, Map4, Map5]
    Map = game_maps[options['map']]
    guards = Map.guards
    board = create_board(Map.size, Map.walls, Map.guards, Map.player, Map.door)
    walls = wall_tiles(Map.walls)
    door = board[Map.door[0]][Map.door[1]]

    if options['player'] == 0:
        player = Map.player
    else:
        player = Map.human

    player_path = a_star.a_star(board, player.position, door.position)
    guards = Coalition.form_coalition(guards)
    traveled = []

def update(agent, action):
    global render_list, player, board

    end_game = False

    if type(player).__name__ == 'PlayerAgent':
        render_list = sum(board, [])
    else:
        render_list = see(player, board)
        render_list.extend(walls)
        render_list.append(door)

    classname = type(agent).__name__
    if classname == 'HumanAgent':
        player_move(board, agent, action)
    elif classname == 'PlayerAgent':
        agent.update(board, player_path, traveled, guards, player, door)
    else:
        agent.update(board, player_path, traveled, guards, player, door)
        pass
    if player.position == door.position or len(player_path) < 1:
        # Win condition
        # TODO: Add win condition logic/display
        print("hello")
        end_game = True

    return end_game


def render():
    RENDERER.game_background()
    for sprite in render_list:
        RENDERER.draw_tile(sprite)

    if type(player).__name__ == 'PlayerAgent':
        RENDERER.draw_path(player_path)

    RENDERER.draw_grid()
    RENDERER.finish_rendering()

    if type(player).__name__ == 'PlayerAgent':
        pygame.time.wait(30)


def create_board(board_width, walls, guards, player, door):
    game_board = [[Tile((x, y)) for y in range(board_width)]
                  for x in range(board_width)]

    for wall in walls:
        game_board[wall[0]][wall[1]].is_wall = True

    for guard in guards:
        game_board[guard.position[0]][guard.position[1]].set_agent(guard)

    game_board[player.position[0]][player.position[1]].set_agent(player)
    game_board[player.position[0]][player.position[1]].is_player = True

    game_board[door[0]][door[1]].is_exit = True

    return game_board


def wall_tiles(wall_coord):
    wall_list = []
    for wall in wall_coord:
        wall_list.append(board[wall[0]][wall[1]])
    return wall_list


#def parse_inputs(inputs):
#    action = ''
#    while (len(inputs['keys']) != 0):
#        action = inputs['keys'][0]
#    return action

def block_parse_inputs(inputs):
    action = ''
    while (len(inputs['keys']) == 0):
        inputs=INPUTS.get_input()
    action = inputs['keys'][0]
    return action



def player_move(board, player, action):
    if(can_move(board, player, action)):
        player.update(action, True, board, guards)
    else:
        player.update(action, False, board, guards)


def can_move(board, player, action):
    move = True
    if(action == 'down'):
        if (player.position[1] == 19
                or board[player.position[0]][player.position[1] + 1].is_wall):
            move = False
    if(action == 'up'):
        if (player.position[1] == 0
                or board[player.position[0]][player.position[1] - 1].is_wall):
            move = False
    if(action == 'left'):
        if (player.position[0] == 0
                or board[player.position[0] - 1][player.position[1]].is_wall):
            move = False
    if(action == 'right'):
        if (player.position[0] == 19
                or board[player.position[0] + 1][player.position[1]].is_wall):
            move = False
    return move

