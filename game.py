from typing import TYPE_CHECKING, Tuple, List, Union
from tile import Tile
from input import Input
from renderer import Renderer
from maps import Map1, Map2, Map3, Map4, Map5
from percept import see, hear

if TYPE_CHECKING:
    from human_agent import HumanAgent
    from player_agent import PlayerAgent
    from guard_agent import GuardAgent

render_list = []
board = []
guards = []
walls = []
player = None
door = None

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
    global guards, board, player, walls, door

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
    board = create_board(Map3.size, Map3.walls, Map3.guards, Map3.player, Map3.door)
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


def update(inputs):
    global render_list
    if player is not None:
        render_list = see(player, board)

    render_list.extend(walls)
    render_list.append(door)

    # for guard in guards:
    #     guard.getSight(get_percepts(guard))
    #     render_list.append(guard.update())

    return False


def render():
    RENDERER.game_background()
    for sprite in render_list:
        RENDERER.draw_tile(sprite)

    RENDERER.draw_grid()
    RENDERER.finish_rendering()


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
