from tile import Tile
from typing import List, Tuple
from abstract_agent import AbstractAgent, KNIFE


class PlayerAgent(AbstractAgent):

    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position)
        self.gold = 100
        self.weapon = KNIFE

    def update(self):
        return self

    def render(self, board: List[List[Tile]]):
        if self.debug:
            for tile in self.look_around(board):
                self.RENDERER.color_tile(tile, self.RENDERER.WHITE)
        self.RENDERER.draw_player(self)
