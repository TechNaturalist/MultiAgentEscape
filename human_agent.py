from typing import List, Tuple
from abstract_agent import AbstractAgent, KNIFE


class HumanAgent(AbstractAgent):

    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position)
        self.gold = 100
        self.weapon = KNIFE
        self.is_player = True
        self.conflict = False

    def update(self, action, can_move):
        if(not self.conflict and can_move):
            if(action == 'up'):
                self.position =(self.position[0], self.position[1] - 1)
            elif( action == 'down'):
                self.position =(self.position[0], self.position[1] + 1)
            elif(action == 'left'):
                self.position =(self.position[0] - 1, self.position[1])
            elif(action == 'right'):
                self.position =(self.position[0] +1, self.position[1])
            else:
                ##conflict menu
                pass

    def render(self, board):
        if self.debug:
            for tile in self.look_around(board):
                self.RENDERER.color_tile(tile, self.RENDERER.WHITE)
        self.RENDERER.draw_player(self)
