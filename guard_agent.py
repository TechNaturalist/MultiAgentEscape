from __future__ import annotations
import random
from tile import Tile
from typing import List, TYPE_CHECKING, Tuple
from abstract_agent import AbstractAgent
from percept import see
import a_star

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
        self.on_trail = None

    def update(self, board: List[List[Tile]],
               player_path: List[Tile],
               traveled,
               guards: List[AbstractAgent],
               player: AbstractAgent,
               door):

        perceive = see(self, board)
        if board[player.position[0]][player.position[1]] in perceive:
            # react to player character
            pass
        elif self.on_trail is not None :
            current_tile = board[self.position[0]][self.position[1]]
            current_tile.set_agent()
            next_pos = self.on_trail.pop(0)
            self.position = next_pos
            board[next_pos[0]][next_pos[1]].set_agent(self)
        elif bool(set(perceive).intersection(self.tiles(traveled, board))):
            self.on_trail = a_star.a_star(board, self.position, door.position)
            current_tile = board[self.position[0]][self.position[1]]
            current_tile.set_agent()
            next_pos = self.on_trail.pop(0)
            self.position = next_pos
            board[next_pos[0]][next_pos[1]].set_agent(self)
        else:
            valid_moves = self.get_valid_neighbor_positions(self.position, board)
            # Guard may not move
            valid_moves.append(self.position)
            new_position = random.choice(valid_moves)

            if new_position != self.position:
                board[self.position[0]][self.position[1]].set_agent()

                board[new_position[0]][new_position[1]].set_agent(self)
                self.position = new_position

    def render(self, board):
        if self.debug:
            for tile in self.look_around(board):
                self.RENDERER.color_tile(tile, self.RENDERER.DARKGRAY)
        self.RENDERER.draw_guard(self)

    def get_valid_neighbor_positions(self, position: Tuple[int, int], board) -> List[Tuple[int, int]]:
        valid_neighbors = []

        valid_deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for i, j in valid_deltas:
            new_x = position[0] + i
            new_y = position[1] + j
            if 0 <= new_x < len(board[0]) and 0 <= new_y < len(board):
                cur_tile = board[new_x][new_y]
                if not cur_tile.is_wall and cur_tile.agent is None:
                    valid_neighbors.append(cur_tile.position)

        return valid_neighbors

    def tiles(self, tile_coord, board):
        tile_list = []
        for coord in tile_coord:
            tile_list.append(board[coord[0]][coord[1]])
        return tile_list
