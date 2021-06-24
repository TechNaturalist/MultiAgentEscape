from __future__ import annotations
from typing import List, Tuple, Union, TYPE_CHECKING


class Tile:
    def __init__(self,
                 position: Tuple[int, int]):
        self.position = position
        self.is_exit = False
        self.is_wall = False
        self.agent = None

    def set_agent(self, agent=None):
        self.agent = agent
