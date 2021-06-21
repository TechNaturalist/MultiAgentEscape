from typing import Tuple
from abstract_agent import AbstractAgent


class Tile:
    def __init__(self,
                 position: Tuple[int, int],
                 is_exit: bool,
                 is_wall: bool,
                 agent: AbstractAgent):
        self.position = position
        self.is_exit = is_exit
        self.is_wall = is_wall
        self.agent = agent

    def set_agent(self, agent=None):
        self.agent = agent
