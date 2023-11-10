from random import randint
from typing import Any, List
from pygame.sprite import Sprite
import pygame as pg

from constants import NB_CHRONON_FISH_PREGNANCY

class Fish(Sprite):
    def __init__(self, groups, image, position, size):
        super().__init__(groups)
        
        percent = 80
        scaled = (percent * size[0])/100 if size[0] < size[1] else (percent * size[1])/100
        image = pg.transform.smoothscale(image, (scaled, scaled))
        self.image = image
        self.rect = self.image.get_rect(center = (position[0] + size[0] / 2, position[1] + size[1] / 2))
        self.setParams(pregnancy=NB_CHRONON_FISH_PREGNANCY)

    def moveRules(self, cellsAround):
        if len(cellsAround) > 0:
            return cellsAround[randint(0, len(cellsAround) - 1)]

        return None
    
    def doReproduce(self):
        self.params['pregnancy'] -= 1

        result = self.params['pregnancy'] == 0
        if result == True:
            self.setParams(pregnancy=NB_CHRONON_FISH_PREGNANCY)

        return result

    def setEnergy(self):
        return None

    def setParams(self, **kwargs):
        if hasattr(self, 'params'):
            self.params.update(kwargs)
        else:
            self.params = dict(kwargs)

    def getParams(self):
        return self.params