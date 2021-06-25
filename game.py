from __future__ import annotations
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

BOARD_WIDTH = 20

#Syntactic sugary goodness
MAPS = [Map1(), Map2(), Map3(), Map4(), Map5()]

def start(options):
    global RENDERER, INPUTS, action

    RENDERER = Renderer.get_instance()
    INPUTS = Inputs.get_instance()
    game_map = False
    action = ''

    game_init(options)

    initiative = [player] + guards

    render()
    while not game_map:
        if type(player).__name__ == 'HumanAgent':
            action = block_parse_inputs(INPUTS.get_input())
        curr_agent = initiative.pop(0)
        # Run agents turn.
        #game_map = update(curr_agent)
        game_map = update(action)
        print(game_map)
        initiative.append(curr_agent)
        render()

    print("returning")
    return

def game_init(options):
    global guards, board, player, walls, door, player_path
    
    MAPS = [Map1(), Map2(), Map3(), Map4(), Map5()]
    Map = MAPS[options['map']]
    guards = Map.guards
    board = create_board(Map.size, Map.walls, Map.guards, Map.player, Map.door)
    walls = wall_tiles(Map.walls)
    door = board[Map.door[0]][Map.door[1]]

    if options['player'] == 0:
        player = Map.player
    else:
        player = Map.human

    player_path = a_star.a_star(board, player.position, door.position)

def update(inputs):
    global render_list, player, board

    end_game = False

    classname = type(player).__name__
    if classname == 'HumanAgent':
        player_move(board, player, action)
        render_list = see(player, board)
        render_list.extend(walls)
        render_list.append(door)
    elif classname == 'PlayerAgent':
        render_list = sum(board, [])

        current_player_tile = board[player.position[0]][player.position[1]]
        current_player_tile.set_agent()

        next_pos = player_path.pop(0)
        player.position = next_pos
        board[next_pos[0]][next_pos[1]].set_agent(player)
    else:
        raise NotImplementedError

    for guard in guards:
        valid_moves = get_valid_neighbor_positions(guard.position)
        # Guard may not move
        valid_moves.append(guard.position)
        new_position = random.choice(valid_moves)

        if new_position != guard.position:
            board[guard.position[0]][guard.position[1]].set_agent()

            board[new_position[0]][new_position[1]].set_agent(guard)
            guard.position = new_position

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
        pygame.time.wait(500)


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


def get_valid_neighbor_positions(position: Tuple[int, int]) -> List[Tuple[int, int]]:
    global board
    valid_neighbors = []

    valid_deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i, j in valid_deltas:
        new_x = position[0] + i
        new_y = position[1] + j
        if 0 <= new_x < len(board[0]) and 0 <= new_y < len(board):
            cur_tile = board[new_x][new_y]
            if not cur_tile.is_wall and cur_tile.agent is None:
                valid_neighbors.append(cur_tile.position)

    return valid_neighbors


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
        remove_player(board, player)
        player.update(action, True)
        move_player(board, player)
    else:
        player.update(action, False)
    # bump


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


def move_player(board, player):
    board[player.position[0]][player.position[1]].set_agent(player)
    board[player.position[0]][player.position[1]].is_player = True


def remove_player(board, player):
    board[player.position[0]][player.position[1]].set_agent(None)
    board[player.position[0]][player.position[1]].is_player = False
