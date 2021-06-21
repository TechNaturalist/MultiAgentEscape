from abstract_agent import AbstractAgent, KNIFE


class PlayerAgent(AbstractAgent):
    
    def __init__(self, position) -> None:
        super().__init__(position)
        self.gold = 100
        self.weapon = KNIFE
