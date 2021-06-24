from typing import TYPE_CHECKING, Tuple, List, Union
from tile import Tile
from inputs import Inputs
from renderer import Renderer
from maps import Map1, Map2
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

BOARD_WIDTH = 20


def start(options):
    global RENDERER, INPUTS, action

    print("hello")
    RENDERER = Renderer.get_instance()
    INPUTS = Inputs.get_instance()
    game_map = False
    action = ''

    game_init(options)

    while not game_map:

        action = parse_inputs( INPUTS.get_input() )
        game_map = update(action)
        render()


def game_init(options):
    global guards, board, player, walls

    # walls = [(10, 10)]
    # guards = [GuardAgent((11, 11))]
    # player = PlayerAgent((12, 12))
    #
    # board = tile.create_board(BOARD_WIDTH, walls, guards, player)

    guards = Map1.guards
    player = Map1.player
    walls = Map1.walls
    board = create_board(Map1.size, Map1.walls, Map1.guards, Map1.player, Map1.door)

    # guards = Map2.guards
    # player = Map2.player
    # walls = Map2.walls
    # board = create_board(Map2.size, Map2.walls, Map2.guards, Map2.player, Map2.door)


def update(action):
    global render_list
    if player is not None:
        player_move(board, player, action)
        render_list = see(player, board)
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

def parse_inputs(inputs):
    action = ''
    if (len(inputs['keys']) != 0):
        action = inputs['keys'][0]
    return action

def player_move(board, player, action):
    if(can_move(board,player, action)):
        remove_player(board, player)
        player.update(action, True)
        move_player(board, player)
    else:
        player.update(action, False)
    #bump

def can_move(board, player, action):
    move = True
    if(action == 'down'):
        if ( player.position[1] == 19
            or board[player.position[0]][player.position[1] + 1].is_wall == True ):
            move = False;
    if(action == 'up'):
        if ( player.position[1] == 0
            or board[player.position[0]][player.position[1] - 1].is_wall == True ):
            move = False;
    if(action == 'left'):
        if ( player.position[0] == 0 
             or board[player.position[0] - 1][player.position[1]].is_wall == True):
            move = False;
    if(action == 'right'):
        if (player.position[0] == 19 
            or board[player.position[0] +1 ][player.position[1]].is_wall == True):
            move = False;
    return move

def move_player(board, player):
    board[player.position[0]][player.position[1]].set_agent(player)
    board[player.position[0]][player.position[1]].is_player = True

def remove_player(board,player):
    board[player.position[0]][player.position[1]].set_agent(None)
    board[player.position[0]][player.position[1]].is_player = False

   
