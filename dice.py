import random


def roll_dice(dice_count: int, dice_sides: int) -> int:
    ret = 0
    for _ in range(dice_count):
        ret += random.randint(1, dice_sides)
    return ret
