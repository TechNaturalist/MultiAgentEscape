from guard_agent import GuardAgent
from typing import List, Tuple, Union
from abstract_agent import AbstractAgent
import numpy as np
from random import randint, random


BRIBE_AMOUNT = 25


def bribe(player: AbstractAgent, agent: GuardAgent)\
        -> Tuple[AbstractAgent, AbstractAgent, bool]:

    # Form matrix:
    #              kill    bribe
    # kill  | gold * (power - perc_power), coalition_gold * (power - perc_power) | gold * (power - perc_power) , bribe_gold |  # noqa: E501
    # bribe |               gold_remaning, gold * (power - perc_power)           |        gold_remaining, bribe_gold        |  # noqa: E501
    #

    if player.gold >= BRIBE_AMOUNT:

        matrix = [[(player.weapon - agent.get_perceived_power(),
                    agent.weapon - player.get_perceived_power()),
                   (player.weapon - agent.get_perceived_power(),
                   BRIBE_AMOUNT)],
                  [(player.gold - agent.get_perceived_power(),
                   player.get_perceived_power()),
                   (player.gold,
                   BRIBE_AMOUNT)]]

        print(f"| {matrix[0][0]} | {matrix[0][1]} |")
        print(f"| {matrix[1][0]} | {matrix[1][1]} |")

        p, q = mixed_strategy_2x2(matrix)

        if p is None or q is None:
            bribe_success = False
            return player, agent, bribe_success

        if 0 < p <= 1 and 0 < q <= 1:
            if (p == 1 and q == 1) or \
                    random() < (1 - p) and random() < (1 - q):
                agent.bribe_offered = True
                player.gold -= BRIBE_AMOUNT
                agent.gold += BRIBE_AMOUNT
                bribe_success = True
                agent.is_bribed = True
                print("The guard accepted the bribe")
                return bribe_success

    bribe_success = False
    print("The guard rejected the bribe...")
    return bribe_success


def mixed_strategy_2x2(matrix: List[List[Tuple[int, int]]]) \
        -> Tuple[Union[float, None], Union[float, None]]:
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


def pure_strategy_2x2(matrix: List[List[Tuple[int, int]]]) \
        -> List[Tuple[int, int]]:
    col_strategies = []
    row_strategies = []

    for i in range(2):
        # Grab the entries in the current column
        col = [matrix[0][i], matrix[1][i]]
        # Find the entry with the maximum value for p1
        p1_max = max(col, key=lambda x: x[0])

        # Grab the entries in the current row
        row = [matrix[i][0], matrix[i][1]]
        # Find the entry with the maximum value for p12
        p2_max = max(row, key=lambda y: y[1])

        for index in range(2):
            if col[index][0] == p1_max[0]:
                # If a column value equals the maximum, add it
                col_strategies.append((index, i))

            if row[index][1] == p2_max[1]:
                # If a row value equals the maximum, add it
                row_strategies.append((i, index))

    # The pure strategies will be the overlap of the column and
    # row strategies
    result = list(set(col_strategies).intersection(set(row_strategies)))

    return result


def get_p_q(matrix: List[List[Tuple[int, int]]]) \
        -> Tuple[float, float]:
    mixed_p, mixed_q = mixed_strategy_2x2(matrix)
    pure_solution = pure_strategy_2x2(matrix)

    # If we have a single pure solution, use it
    if len(pure_solution) == 1:
        p = pure_solution[0][1]
        q = pure_solution[0][0]
    # If any mixed number is None, use a random p/q
    # from 0-1
    elif mixed_p is None and mixed_q is None:
        p = random()
        q = random()
    elif mixed_p is not None and mixed_q is None:
        p = mixed_p
        q = random()
    elif mixed_p is None and mixed_q is not None:
        p = random()
        q = mixed_q
    # If we have a valid set of mixed solutions, use them
    elif mixed_p is not None and mixed_q is not None and \
            0 <= mixed_p <= 1 and 0 <= mixed_q <= 1:
        p = mixed_p
        q = mixed_q
    # If we have two pure solutions and bad mixed solutions,
    # we have a strategy we can remove. We can find it by
    # removing the solution with the least social welfare
    elif len(pure_solution) == 2:
        first = matrix[pure_solution[0][0]][pure_solution[0][1]]
        second = matrix[pure_solution[1][0]][pure_solution[1][1]]
        if sum(first) > sum(second):
            p = pure_solution[0][0]
            q = pure_solution[0][1]
        else:
            p = pure_solution[1][0]
            q = pure_solution[1][1]
    # Catch any issues/unresolved values here
    else:
        raise NotImplementedError

    return p, q


def matrix_test():
    matrix = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    result = pure_strategy_2x2(matrix)
    assert matrix[result[0][0]][result[0][1]] == (7, 8)

    for _ in range(1000):
        matrix = [[(randint(0, 9), randint(0, 9)),
                   (randint(0, 9), randint(0, 9))],
                  [(randint(0, 9), randint(0, 9)),
                  (randint(0, 9), randint(0, 9))]]

        p, q = get_p_q(matrix)
        print(p, q)


if __name__ == '__main__':
    matrix_test()
