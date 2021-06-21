import random
from tile import Tile
from typing import List
from coalition import Coalition
from abstract_agent import AbstractAgent
from Renderer import Renderer

attitude = {
    'nice': 5,
    'neutral': 3,
    'mean': 1,
}


class GuardAgent(AbstractAgent):
    RENDERER = Renderer.get_instance()

    def __init__(self, position) -> None:
        super().__init__(position)
        self.coalition: Coalition
        self.skill = random.randint(1, 5)
        self.attitude = random.choice(list(attitude.values()))
        self.is_bribed = False
        self.bribe_offered = False

    def update(self):
        return self

    def render(self, board: List[List[Tile]]):
        if self.debug:
            for tile in self.look_around():
                self.RENDERER.color_tile(tile,  self.RENDERER.CORAL)
        self.RENDERER.draw_guard(self.position)
