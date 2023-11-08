import pygame as pg

from components.fish import Fish


class Shark(Fish):
    def __init__(self, group, image, x, y, width, height):
        super().__init__(group, image, x, y, width, height)