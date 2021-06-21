from typing import List
from guard_agent import GuardAgent


class Coalition:
    def __init__(self) -> None:
        self.members: List[GuardAgent]

    def form_coalition(self, potential_members: List[GuardAgent]):
        pass

    def __form_coalition_test(self, potential_members: List[GuardAgent]):
        self.members = potential_members
        for member in potential_members:
            member.coalition = self

    def calculate_coalition_utility(self, potential_members: List[GuardAgent]) -> float:
        utility = 0

        # Add utility of all potential members
        for member in potential_members:
            utility += member.attitude + member.weapon

        # The total utility is the utility of each potential member divided by the number of people ^ 1.3
        utility = utility / ((len(potential_members) + 1) ** 1.3)

        return utility
