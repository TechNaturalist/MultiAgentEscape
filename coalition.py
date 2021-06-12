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
