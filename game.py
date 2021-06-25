"""The main game logic

Written by: Dick Loveland, Nathan Holst, Max Clark
"""
from __future__ import annotations
from coalition import Coalition
from typing import Tuple, List
import pygame
from tile import Tile
from inputs import Inputs
from renderer import Renderer
from maps import Map1, Map2, Map3, Map4, Map5
from percept import see, hear
import a_star

BOARD_WIDTH = 20


class Game:
    RENDERER = Renderer.get_instance()
    INPUTS = Inputs.get_instance()

    def __init__(self):
        self.game_map = False
        self.render_list = []
        self.board = []
        self.guards = []
        self.walls = []
        self.Map = None
        self.player = None
        self.door = None
        self.player_path = None
        self.traveled = []
        self.initiative = []

    def start(self, options):

        self.game_init(options)
        self.initiative = [self.player] + self.guards
        self.update(self.player, '')
        self.render()
        while not self.game_map:
            curr_agent = self.initiative.pop(0)
            action = ''
            if (type(self.player).__name__ == 'HumanAgent'
                    and type(curr_agent).__name__ == 'HumanAgent'):
                action = self.block_parse_inputs(Game.INPUTS.get_input())
            # Run agents turn.
            self.game_map = self.update(curr_agent, action)
            self.initiative.append(curr_agent)
            self.render()
        if self.player.gold == 0:
            print("The Thief was captured and the gold was returned.")
        else:
            print(f"The Thief escaped with {self.player.gold} gold!")
        return self.player.gold

    def game_init(self, options):
        game_maps = [Map1(), Map2(), Map3(), Map4(), Map5()]
        self.Map = game_maps[options['map']]
        self.guards = self.Map.guards
        self.board = self.create_board(
            self.Map.size, self.Map.walls, self.Map.guards, self.Map.player, self.Map.door)
        self.walls = self.wall_tiles(self.Map.walls)
        self.door = self.board[self.Map.door[0]][self.Map.door[1]]

        if options['player'] == 0:
            self.player = self.Map.player
        else:
            self.player = self.Map.human

        self.player_path = a_star.a_star(
            self.board, self.player.position, self.door.position)
        self.guards = Coalition.form_coalition(self.guards)
        self.traveled = []

    def update(self, agent, action):

        end_game = False

        if type(self.player).__name__ == 'PlayerAgent':
            self.render_list = sum(self.board, [])
        else:
            self.render_list = see(self.player, self.board)
            self.render_list.extend(self.walls)
            self.render_list.append(self.door)

        classname = type(agent).__name__
        if classname == 'HumanAgent':
            self.player_move(self.board, agent, action)
        elif classname == 'PlayerAgent':
            agent.update(self.board, self.player_path, self.traveled,
                         self.guards, self.player, self.door)
        else:
            agent.update(self.board, self.player_path, self.traveled,
                         self.guards, self.player, self.door)

        if self.player.position == self.door.position or len(self.player_path) < 1:
            # Win condition
            # TODO: Add win condition logic/display
            end_game = True

        return end_game

    def render(self):
        Game.RENDERER.game_background()
        if type(self.player).__name__ == 'PlayerAgent':
            Game.RENDERER.draw_path(self.player_path)

        for sprite in self.render_list:
            Game.RENDERER.draw_tile(sprite)

        Game.RENDERER.draw_grid()
        Game.RENDERER.finish_rendering()

        if type(self.player).__name__ == 'PlayerAgent':
            pygame.time.wait(30)

    def create_board(self, board_width, walls, guards, player, door):
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

    def wall_tiles(self, wall_coord):
        wall_list = []
        for wall in wall_coord:
            wall_list.append(self.board[wall[0]][wall[1]])
        return wall_list


# def parse_inputs(inputs):
#    action = ''
#    while (len(inputs['keys']) != 0):
#        action = inputs['keys'][0]
#    return action

    def block_parse_inputs(self, inputs):
        action = ''
        while (len(inputs['keys']) == 0):
            inputs = INPUTS.get_input()
        action = inputs['keys'][0]
        return action

    def player_move(self, board, player, action):
        if(can_move(board, player, action)):
            player.update(action, True, board, guards)
        else:
            player.update(action, False, board, guards)

    def can_move(self, board, player, action):
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
