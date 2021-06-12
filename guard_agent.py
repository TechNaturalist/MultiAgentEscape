import random
from coalition import Coalition
from abstract_agent import AbstractAgent

attitude = {
    'nice': 1,
    'neutral': 3,
    'mean': 5,
}


class GuardAgent(AbstractAgent):

    def __init__(self, position) -> None:
        super().__init__(position)
        self.coalition: Coalition
        self.skill = random.randint(1, 5)
        self.attitude = random.choice(list(attitude.keys()))
