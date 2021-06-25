"""A D&D style dice calculator

Written by: Max Clark
"""
import random


def roll_dice(dice_count: int, dice_sides: int) -> int:
    """Rolls a number of dice with a number of sides
    and gives the result.

    Args:
        dice_count (int): The number of dice
        dice_sides (int): The sides of the dice

    Returns:
        int: The resulting random dice throw
    """
    ret = 0
    for _ in range(dice_count):
        ret += random.randint(1, dice_sides)
    return ret
