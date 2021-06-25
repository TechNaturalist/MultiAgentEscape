"""A class to handle human players playing as
the thief.

Written by: Max Clark, Nathan Holst
"""
from __future__ import annotations
from typing import List, TYPE_CHECKING, Tuple
from abstract_agent import AbstractAgent, KNIFE
from percept import see

if TYPE_CHECKING:
    from tile import Tile


class HumanAgent(AbstractAgent):

    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position)
        self.gold = 100
        self.weapon = KNIFE
        self.is_player = True
        self.conflict = False

    def update(self,
               board: List[List[Tile]],
               player_path: List[Tile],
               traveled,
               guards: List[AbstractAgent],
               player: AbstractAgent,
               door: Tile,
               can_move):

        perceive = see(self, board)
        # is_guard = None
        g_list = self.guard_tiles(guards, board)
        for g in g_list:
            if g in perceive:
                # is_guard = g
                self.conflict = True

        if not self.conflict and can_move:
            board[self.position[0]][self.position[1]].set_agent()
            if action == 'up':
                self.position = (self.position[0], self.position[1] - 1)
            elif action == 'down':
                self.position = (self.position[0], self.position[1] + 1)
            elif action == 'left':
                self.position = (self.position[0] - 1, self.position[1])
            elif action == 'right':
                self.position = (self.position[0] + 1, self.position[1])
            board[self.position[0]][self.position[1]].set_agent(self)
        else:
            # conflict menu
            pass

    def render(self, board):
        if self.debug:
            for tile in self.look_around(board):
                self.RENDERER.color_tile(tile, self.RENDERER.WHITE)
        self.RENDERER.draw_player(self)

    def guard_tiles(self, guard_obj, board):
        guard_list = []
        for guard in guard_obj:
            guard_list.append(board[guard.position[0]][guard.position[1]])
        return guard_list
