from typing import List, Tuple
from abstract_agent import AbstractAgent
import numpy as np
from random import randint, random
from fractions import Fraction


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


def mixed_strategy_2x2(matrix: List[List[Tuple[int, int]]]):
    """Solve using mixed strategy algorithm from
    https://www3.nd.edu/~apilking/Math10120/Lectures/Topic%2029.pdf
    Page 3

    Args:
        matrix (List[List[Tuple[int, int]]]): An array of the matrix
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

    return (p, q)


def pure_strategy_2x2(matrix):
    col_strategies = []
    row_strategies = []

    for i in range(2):
        col = [matrix[0][i], matrix[1][i]]
        p2_max = max(col, key=lambda x: x[0])

        row = [matrix[i][0], matrix[i][1]]
        p1_max = max(row, key=lambda y: y[1])

        for index in range(2):
            if col[index][0] == p2_max[0]:
                col_strategies.append((index, i))

            if row[index][1] == p1_max[1]:
                row_strategies.append((i, index))

    result = list(set(col_strategies).intersection(set(row_strategies)))

    return result


def get_p_q(matrix):
    mixed_p, mixed_q = mixed_strategy_2x2(matrix)
    pure_solution = pure_strategy_2x2(matrix)

    if len(pure_solution) == 1:
        p = pure_solution[0][1]
        q = pure_solution[0][0]
    elif mixed_p is None and mixed_q is None:
        p = random()
        q = random()
    elif mixed_p is not None and mixed_q is None:
        p = mixed_p
        q = random()
    elif mixed_p is None and mixed_q is not None:
        p = random()
        q = mixed_q
    elif 0 <= mixed_p <= 1 and 0 <= mixed_q <= 1:
        p = mixed_p
        q = mixed_q
    elif len(pure_solution) == 2:
        first = matrix[pure_solution[0][0]][pure_solution[0][1]]
        second = matrix[pure_solution[1][0]][pure_solution[1][1]]
        if sum(first) > sum(second):
            p = pure_solution[0][0]
            q = pure_solution[0][1]
        else:
            p = pure_solution[1][0]
            q = pure_solution[1][1]
    else:
        raise NotImplementedError

    return p, q


def matrix_test():
    matrix = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    result = pure_strategy_2x2(matrix)
    print(result)

    for _ in range(1000):
        matrix = [[(randint(0, 9), randint(0, 9)), (randint(0, 9), randint(0, 9))],
                  [(randint(0, 9), randint(0, 9)), (randint(0, 9), randint(0, 9))]]

        get_p_q(matrix)


if __name__ == '__main__':
    matrix_test()
