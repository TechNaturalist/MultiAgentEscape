from __future__ import annotations
from typing import List, Tuple, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from human_agent import HumanAgent
    from player_agent import PlayerAgent
    from guard_agent import GuardAgent
    from abstract_agent import AbstractAgent


class Tile:
    def __init__(self,
                 position: Tuple[int, int]):
        self.position = position
        self.is_exit = False
        self.is_wall = False
        self.agent: AbstractAgent

    def set_agent(self, agent=None):
        self.agent = agent

    @staticmethod
    def create_board(board_width: int,
                     walls: List[Tuple[int, int]],
                     guards: List[GuardAgent],
                     player: Union[PlayerAgent, HumanAgent])\
            -> List[list[Tile]]:

        board = [[Tile((x, y)) for x in range(board_width)]
                 for y in range(board_width)]

        for wall in walls:
            board[wall[0]][wall[1]].is_wall = True

        for guard in guards:
            board[guard.position[0]][guard.position[1]].agent = guard

        board[player.position[0]][player.position[1]].agent = player

        return board
