import random
from coalition import Coalition
from abstract_agent import AbstractAgent

attitude = {
    'nice': 5,
    'neutral': 3,
    'mean': 1,
}


class GuardAgent(AbstractAgent):
    def __init__(self, position) -> None:
        super().__init__(position)
        self.coalition: Coalition
        self.skill = random.randint(1, 5)
        self.attitude = random.choice(list(attitude.values()))
        self.is_bribed = False
