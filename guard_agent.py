from __future__ import annotations
import random
from tile import Tile
from typing import List, TYPE_CHECKING, Tuple
from abstract_agent import AbstractAgent

if TYPE_CHECKING:
    from coalition import Coalition

attitude = {
    'nice': 5,
    'neutral': 3,
    'mean': 1,
}


class GuardAgent(AbstractAgent):
    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position)
        self.coalition = None
        self.skill = random.randint(1, 5)
        self.attitude = random.choice(list(attitude.values()))
        self.is_bribed = False
        self.bribe_offered = False

    def update(self):
        return self

    def render(self, board):
        if self.debug:
            for tile in self.look_around(board):
                self.RENDERER.color_tile(tile, self.RENDERER.DARKGRAY)
        self.RENDERER.draw_guard(self)
