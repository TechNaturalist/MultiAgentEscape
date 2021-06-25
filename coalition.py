import random
from typing import Dict, List
from guard_agent import GuardAgent

colors = {
    "WHITE": (255, 255, 255),
    "BLACK": (0,   0,   0),
    "BLUE": (0,   0, 255),
    "GREEN": (0, 255,   0),
    "DARKGREEN": (0, 155,   0),
    "DARKGRAY": (40,  40,  40),
    "GRAY": (100, 100, 100),
    "PURPLE": (155,   0, 155),
    "YELLOW": (255, 255,   0),
    "BGCOLOR": (0,   0,   0),
    "RED": (255,   0,   0),
    "CORAL": (255,  77,  77),
}


class Coalition:
    def __init__(self, member_count: int) -> None:
        self.color = random.choice(list(colors.keys()))
        self.member_count = member_count

    @staticmethod
    def form_coalition(guards: List[GuardAgent]) -> List[GuardAgent]:
        print("Guards forming coalition")
        a = guards[0]
        b = guards[1]
        c = guards[2]
        v = {}  # subset values
        v['a'] = a.weapon
        v['b'] = b.weapon
        v['c'] = c.weapon
        v['ab'] = a.attitude + b.attitude + v['a'] + v['b']
        v['ac'] = a.attitude + c.attitude + v['a'] + v['c']
        v['bc'] = c.attitude + b.attitude + v['c'] + v['b']
        v['abc'] = ((v['ab'] + v['ac'] + v['bc']) / 2) ** 0.8

        print(f"{{a}} = {v['a']}")
        print(f"{{b}} = {v['b']}")
        print(f"{{c}} = {v['c']}")
        print(f"{{ab}} = {v['ab']}")
        print(f"{{ac}} = {v['ac']}")
        print(f"{{bc}} = {v['bc']}")
        print(f"{{abc}} = {v['abc']}")

        a_shap, b_shap, c_shap = Coalition.shapley_calc_3x(v)

        if v['ab'] + v['c'] < v['abc'] and \
            v['ac'] + v['b'] < v['abc'] and \
                v['bc'] + v['a'] < v['abc']:
            print("All guards joined coalition")
            coalition = Coalition(3)
            a.coalition = coalition
            b.coalition = coalition
            c.coalition = coalition
            return [a, b, c]

        if v['a'] + v['c'] > v['ac']:
            print("AC coalition")
            coalition = Coalition(2)
            a.coalition = coalition
            c.coalition = coalition
            b.coalition = Coalition(1)
            return [a, b, c]

        if v['a'] + v['b'] > v['ab']:
            print("AB coalition")
            coalition = Coalition(2)
            a.coalition = coalition
            b.coalition = coalition
            c.coalition = Coalition(1)
            return [a, b, c]

        if v['b'] + v['c'] > v['bc']:
            print("BC coalition")
            coalition = Coalition(2)
            c.coalition = coalition
            b.coalition = coalition
            a.coalition = Coalition(1)
            return [a, b, c]

        print("No coalition formed")
        return [a, b, c]

    @staticmethod
    def shapley_calc_3x(values: Dict[str, float]):
        a_count = 0
        b_count = 0
        c_count = 0

        # 123, 132, 213, 231, 312, 321
        a_count += values['a']  # 123
        a_count += values['a']  # 132
        a_count += values['ab'] - values['b']  # 213
        a_count += values['abc'] - values['bc']  # 231
        a_count += values['ac'] - values['c']  # 312
        a_count += values['abc'] - values['bc']  # 321

        # 123, 132, 213, 231, 312, 321
        b_count += values['b']  # 213
        b_count += values['b']  # 231
        b_count += values['ab'] - values['a']  # 123
        b_count += values['abc'] - values['ac']  # 132
        b_count += values['abc'] - values['ac']  # 312
        b_count += values['bc'] - values['c']  # 321

        # 123, 132, 213, 231, 312, 321
        c_count += values['c']  # 312
        c_count += values['c']  # 321
        c_count += values['abc'] - values['ab']  # 213
        c_count += values['bc'] - values['b']  # 231
        c_count += values['abc'] - values['ab']  # 123
        c_count += values['ac'] - values['a']  # 132

        a_count /= 6
        b_count /= 6
        c_count /= 6

        print(f"Shapley values: a = {a_count}, b = {b_count}, c = {c_count}")

        return a_count, b_count, c_count

