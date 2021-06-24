from __future__ import annotations
from typing import Tuple, List

import pygame
from tile import Tile
from input import Input
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
    global guards, board, player, walls, door, player_path

    # walls = [(10, 10)]
    # guards = [GuardAgent((11, 11))]
    # player = PlayerAgent((12, 12))
    #
    # board = tile.create_board(BOARD_WIDTH, walls, guards, player)

    # guards = Map1.guards
    # player = Map1.player
    # board = create_board(Map1.size, Map1.walls, Map1.guards, Map1.player, Map1.door)
    # walls = wall_tiles(Map1.walls)
    # door = board[Map1.door[0]][Map1.door[1]]

    # guards = Map2.guards
    # player = Map2.player
    # board = create_board(Map2.size, Map2.walls, Map2.guards, Map2.player, Map2.door)
    # walls = wall_tiles(Map2.walls)
    # door = board[Map2.door[0]][Map2.door[1]]

    guards = Map3.guards
    player = Map3.player
    board = create_board(Map3.size, Map3.walls,
                         Map3.guards, Map3.player, Map3.door)
    walls = wall_tiles(Map3.walls)
    door = board[Map3.door[0]][Map3.door[1]]

    # guards = Map4.guards
    # player = Map4.player
    # board = create_board(Map4.size, Map4.walls, Map4.guards, Map4.player, Map4.door)
    # walls = wall_tiles(Map4.walls)
    # door = board[Map4.door[0]][Map4.door[1]]
    #
    # guards = Map5.guards
    # player = Map5.player
    # board = create_board(Map5.size, Map5.walls, Map5.guards, Map5.player, Map5.door)
    # walls = wall_tiles(Map5.walls)
    # door = board[Map5.door[0]][Map5.door[1]]

    player_path = a_star.a_star(board, player.position, door.position)


def update(inputs):
    global render_list, player, board

    if player.position == door.position or len(player_path) < 1:
        # Win condition
        # TODO: Add win condition logic/display
        return True

    classname = type(player).__name__
    if classname == 'HumanAgent':
        render_list = see(player, board)
        render_list.extend(walls)
        render_list.append(door)
    elif classname == 'PlayerAgent':
        render_list = sum(board, [])
    else:
        raise NotImplementedError

    current_player_tile = board[player.position[0]][player.position[1]]
    current_player_tile.set_agent()

    next_player_position = player_path.pop(0)
    player.position = next_player_position
    board[next_player_position[0]][next_player_position[1]].set_agent(player)

    for guard in guards:
        valid_moves = get_valid_neighbor_positions(guard.position)
        # Guard may not move
        valid_moves.append(guard.position)
        new_position = random.choice(valid_moves)

        if new_position != guard.position:
            board[guard.position[0]][guard.position[1]].set_agent()

            board[new_position[0]][new_position[1]].set_agent(guard)
            guard.position = new_position

    # for guard in guards:
    #     guard.getSight(get_percepts(guard))
    #     render_list.append(guard.update())

    return False


def render():
    RENDERER.game_background()
    for sprite in render_list:
        RENDERER.draw_tile(sprite)

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
