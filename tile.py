"""A class to represent one tile on the game board

Written by: Max Clark, Nathan Holst
"""
from typing import Tuple


class Tile:
    def __init__(self,
                 position: Tuple[int, int]):
        self.position = position
        self.is_exit = False
        self.is_wall = False
        self.agent = None

    def set_agent(self, agent=None):
        self.agent = agent
