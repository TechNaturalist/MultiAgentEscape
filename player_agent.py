from typing import List, Tuple
from abstract_agent import AbstractAgent, KNIFE
from percept import see
import bargain
import tile


class PlayerAgent(AbstractAgent):

    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(position)
        self.hp = 10
        self.total_hp = 10
        self.gold = 100
        self.weapon = KNIFE
        self.is_player = True
        self.conflict = False

    def update(self, board, player_path, traveled, guards, player, door):
        perceive = see(self, board)
        is_guard = None
        g_list = self.guard_tiles(guards, board)
        for g in g_list:
            if g in perceive:
                is_guard = g

        current_player_tile = board[self.position[0]][self.position[1]]
        current_player_tile.set_agent()

        if self.conflict:
            current_player_tile.set_agent(self)
            # FIGHT!
            print("The Thief attacks the guard with his knife!")
            won = is_guard.agent.damage(self.weapon)
            if won:
                print("The Thief killed a guard!")
                guards.remove(is_guard.agent)
                self.conflict = False
        else:
            if is_guard is None:
                next_pos = player_path.pop(0)
                traveled.append(self.position)
                self.position = next_pos
                board[next_pos[0]][next_pos[1]].set_agent(self)
            else:
                current_player_tile.set_agent(self)
                # react to guard
                is_guard.agent.is_bribed = bargain.bribe(self, is_guard.agent)
                if is_guard.agent.is_bribed:
                    is_guard.agent.gold += 25
                    self.gold -= 25
                    guards.remove(is_guard.agent)
                else:
                    self.conflict = True
                    is_guard.agent.bribe_offered = True

    def render(self, board):
        if self.debug:
            for tile in self.look_around(board):
                self.RENDERER.color_tile(tile, self.RENDERER.WHITE)
        self.RENDERER.draw_player(self)

    def guard_tiles(self, guard_obj, board):
        guard_list = []
        for guard in guard_obj:
            guard_list.append(board[guard.position[0]][guard.position[1]])
        return guard_list

    def damage(self, hit):
        self.hp -= hit
        if self.hp <= 0:
            return True
        return False
