from typing import List
from abstract_agent import AbstractAgent


class HumanAgent(AbstractAgent):
    def __init__(self, position) -> None:
        super().__init__(position)

    def get_movement(self):
        """Get the current player movement from pygame. Not necessary when an
        agent player is playing."""
        pass

    def update(self):
        return self

    def render(self, board):
        if self.debug:
            for tile in self.look_around(board):
                self.RENDERER.color_tile(tile, self.RENDERER.WHITE)
        self.RENDERER.draw_player(self)
