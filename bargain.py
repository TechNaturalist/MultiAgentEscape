from typing import Tuple
from abstract_agent import AbstractAgent


def bribe(player: AbstractAgent, agent: AbstractAgent, value: int) -> Tuple[AbstractAgent, AbstractAgent]:
    if player.gold >= value:
        # TODO: Calculate bribe here based on criteria
        pass

    return player, agent
