from abstract_agent import AbstractAgent


class Player(AbstractAgent):
    def __init__(self, position) -> None:
        super().__init__(position)

    def get_movement(self):
        """Get the current player movement from pygame. Not necessary when an agent player is playing."""
        pass