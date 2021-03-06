"""Input gathering through pygame for the game.

Written by: Dick Loveland
"""
import pygame
from pygame.locals import K_w, K_s, K_a, K_d, KEYDOWN, K_ESCAPE, K_RETURN

import helper

defaults = {
    "up": K_w,
    "down": K_s,
    "left": K_a,
    "right": K_d
}


class Inputs:
    __instance = None

    @staticmethod
    def get_instance():
        if Inputs.__instance is None:
            Inputs()
        return Inputs.__instance

    def __init__(self):
        if Inputs.__instance is not None:
            raise Exception("this class is a singleton!")
        else:
            self.map = defaults
            print(defaults)
            self.currentInputs = {}
            self.keys = []
            self.mouse = {}
            Inputs.__instance = self

    def set_inputs(self, location, key):
        self.map[location] = key

    def get_keys(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                helper.terminate()
            if (event.type == KEYDOWN):
                if (event.key == self.map["up"]):
                    self.keys.append('up')
                elif (event.key == self.map["down"]):
                    self.keys.append('down')
                elif (event.key == self.map["left"]):
                    self.keys.append('left')
                elif (event.key == self.map["right"]):
                    self.keys.append('right')
                elif (event.key == K_ESCAPE):
                    self.keys.append('back')
                elif (event.key == K_RETURN):
                    self.keys.append('enter')

    def get_mouse(self):
        pass

    def get_input(self):
        self.keys = []
        self.mouse = {}
        self.get_mouse()
        self.get_keys()

        return {
            "mouse": self.mouse,
            "keys": self.keys
        }
