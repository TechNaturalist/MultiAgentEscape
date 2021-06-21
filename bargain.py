from typing import Tuple
from abstract_agent import AbstractAgent


BRIBE_AMOUNT = 25

def bribe(player: AbstractAgent, agent: AbstractAgent) -> Tuple[AbstractAgent, AbstractAgent]:

    # Form matrix:
    #              kill    bribe
    # kill  | gold * (power - perc_power), coalition_gold * (power - perc_power) | gold * (power - perc_power) , bribe_gold |
    # bribe |               gold_remaning, gold * (power - perc_power)           |        gold_remaining, bribe_gold        |

    if player.gold >= BRIBE_AMOUNT:
        # TODO: Calculate bribe here based on criteria
        pass

    return player, agent
