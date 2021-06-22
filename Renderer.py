from human_agent import HumanAgent
from player_agent import PlayerAgent
from guard_agent import GuardAgent
from abstract_agent import AbstractAgent
from tile import Tile
from typing import Optional, Tuple, Union
import pygame
import math
from pygame.locals import *

WIDTH = 640
HEIGHT = 640
CELLSIZE = 32
RADIUS = math.floor(CELLSIZE/2.5)
assert WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WIDTH / CELLSIZE)
CELLHEIGHT = int(HEIGHT / CELLSIZE)

pygame.init()


class Renderer:

    __instance = None

    #		R    G    B
    WHITE = (255, 255, 255)
    BLACK = (0,   0,   0)
    GREEN = (0, 255,   0)
    DARKGREEN = (0, 155,   0)
    DARKGRAY = (40,  40,  40)
    GRAY = (100, 100, 100)
    PURPLE = (155,   0, 155)
    YELLOW = (255, 255,   0)
    BGCOLOR = (0,   0,   0)
    RED = (255,   0,   0)
    CORAL = (255,  77,  77)

    @staticmethod
    def get_instance():
        if Renderer.__instance is None:
            Renderer()
        return Renderer.__instance

    def __init__(self):
        if Renderer.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            self.display = pygame.display.set_mode((HEIGHT, WIDTH))
            self.MENUFONT = pygame.font.Font('freesansbold.ttf', 24)
            self.TITLEFONT = pygame.font.Font('freesansbold.ttf', 36)
            self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
            Renderer.__instance = self

    def draw_text(self,
                  text: str,
                  center: dict,
                  font: str,
                  color: Union[int, Tuple[int, int, int, Optional[int]]]):
        if (font == 'basic'):
            surf = self.BASICFONT.render(text, True, color)
            rect = surf.get_rect()
            rect.topleft = (width(center['x']) - 9, height(center['y']) - 9)
        elif (font == 'menu'):
            surf = self.MENUFONT.render(text, True, color)
            rect = surf.get_rect()
            rect.topleft = (width(center['x']) - 12, height(center['y']) - 12)
        elif (font == 'title'):
            surf = self.TITLEFONT.render(text, True, color)
            rect = surf.get_rect()
            rect.topleft = (width(center['x']) - 18, height(center['y']) - 18)
        else:
            raise NotImplementedError
        self.display.blit(surf, rect)

    def draw_guard(self, guard: GuardAgent):
        xcenter = guard.position[0] * CELLSIZE + math.floor(CELLSIZE/2)
        ycenter = guard.position[1] * CELLSIZE + math.floor(CELLSIZE/2)
        pygame.draw.circle(self.display,
                           Renderer.RED,
                           (xcenter, ycenter),
                           RADIUS)

    def draw_player(self, guard: Union[PlayerAgent, HumanAgent]):
        xcenter = guard.position[0] * CELLSIZE + math.floor(CELLSIZE/2)
        ycenter = guard.position[1] * CELLSIZE + math.floor(CELLSIZE/2)
        pygame.draw.circle(self.display,
                           Renderer.RED,
                           (xcenter, ycenter),
                           RADIUS)

    def draw_grid(self):
        for x in range(0, WIDTH, CELLSIZE):
            pygame.draw.line(self.display,
                             Renderer.BGCOLOR,
                             (x, 0),
                             (x, HEIGHT))

        for y in range(0, HEIGHT, CELLSIZE):
            pygame.draw.line(self.display,
                             Renderer.BGCOLOR,
                             (0, y),
                             (WIDTH, y))

    def color_tile(self,
                   tile: Tile,
                   color: Union[int, Tuple[int, int, int, Optional[int]]]):
        x = tile.position[0] * CELLSIZE
        y = tile.position[1] * CELLSIZE
        tile_rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(self.display, color, tile_rect)

    def menu_background(self):
        self.display.fill(Renderer.BLACK)

    def game_background(self):
        self.display.fill(self.DARKGRAY)

    def finish_rendering(self):
        pygame.display.update()


def width(x):
    return int(WIDTH * x / 100)


def height(y):
    return int(HEIGHT * y / 100)
