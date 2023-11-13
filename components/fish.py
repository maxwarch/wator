from random import randint
from typing import Any, List
from pygame.sprite import Sprite
import pygame as pg

from constants import NB_CHRONON_FISH_PREGNANCY

class Fish(Sprite):
    def __init__(self, groups, image, position, size):
        super().__init__(groups)
        self.size = size
        
        percent = 80
        self.scaled = (percent * size[0])/100 if size[0] < size[1] else (percent * size[1])/100
        self.icon = pg.transform.smoothscale(image, (self.scaled, self.scaled))
        self.image = pg.Surface(self.size)
        self.rect = self.icon.get_rect(center = (position[0] + size[0] / 2, position[1] + size[1] / 2))
        self.hide()
        self.setParams(pregnancy=NB_CHRONON_FISH_PREGNANCY)

    def hide(self):
        self.image.set_alpha(0)

    def show(self):
        self.image = self.icon
        self.image.set_alpha(255)

    def moveRules(self, cellsAround):
        cellsAround = [cell for cell in cellsAround if cell.type == None]
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