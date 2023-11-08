import pygame as pg

from components.fish import Fish


class Shark(Fish):
    def __init__(self, group, image, position, size):
        super().__init__(group, image, position, size)