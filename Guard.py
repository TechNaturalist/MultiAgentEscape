from Renderer import Renderer


class Guard:
    RENDERER = Renderer.get_instance()

    def __init__(self, debug, position):
        self.debug = debug
        self.position = position
        self.sight = []

    def update(self):
        return self

    def render(self):
        if self.debug:
            for tile in self.sight:
                Guard.RENDERER.color_tile(tile,  Guard.RENDERER.CORAL)
        Guard.RENDERER.draw_guard(self.position)

    def get_sight(self, tiles):
        self.sight = tiles
