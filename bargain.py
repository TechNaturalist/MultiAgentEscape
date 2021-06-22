from typing import Tuple
from abstract_agent import AbstractAgent
import numpy as np


BRIBE_AMOUNT = 25


def bribe(player: AbstractAgent, agent: AbstractAgent)\
        -> Tuple[AbstractAgent, AbstractAgent]:

    # Form matrix:
    #              kill    bribe
    # kill  | gold * (power - perc_power), coalition_gold * (power - perc_power) | gold * (power - perc_power) , bribe_gold |  # noqa: E501
    # bribe |               gold_remaning, gold * (power - perc_power)           |        gold_remaining, bribe_gold        |  # noqa: E501
    #

    if player.gold >= BRIBE_AMOUNT:
        # TODO: Calculate bribe here based on criteria
        pass

    return player, agent


def solve_matrix(matrix):
    """Solve using mixed strategy algorithm from
    https://www3.nd.edu/~apilking/Math10120/Lectures/Topic%2029.pdf
    Page 3

    Also checks for dominant strategies

    Args:
        matrix (np.array): An np array of the matrix
        in [[(1,2),(3,4)],[(5,6),(7,8)]] format

    Returns:
        Tuple[float, float]: p, q
    """
    m = np.array(matrix)

    c_a = m[0, 0][1]
    c_b = m[1, 0][1]
    c_c = m[0, 1][1]
    c_d = m[1, 1][1]

    r_a = m[0, 0][0]
    r_b = m[1, 0][0]
    r_c = m[0, 1][0]
    r_d = m[1, 1][0]

    p = None
    if (c_a - c_b - c_c + c_d) != 0:
        p = (c_d - c_b)/(c_a - c_b - c_c + c_d)

    q = None
    if (r_a - r_b - r_c + r_d) != 0:
        q = (r_d - r_c)/(r_a - r_b - r_c + r_d)

    if p is None or q is None:
        return (0, 0)
    elif 0 <= p <= 1 and 0 <= q <= 1:
        return (p, q)
    else:
        pass


def matrix_test():
    matrix = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    print(solve_matrix(matrix))
    matrix = [[(5, 2), (3, 2)], [(1, 2), (3, 5)]]
    print(solve_matrix(matrix))


if __name__ == '__main__':
    matrix_test()
