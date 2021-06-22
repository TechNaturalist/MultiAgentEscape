from typing import List, Tuple, Union


class Tile:
    def __init__(self,
                 position: Tuple[int, int]):
        self.position = position
        self.is_exit = False
        self.is_wall = False
        self.agent = None

    def set_agent(self, agent=None):
        self.agent = agent
