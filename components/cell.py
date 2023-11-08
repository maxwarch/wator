from typing import Any, Iterable, Union
import pygame as pg
from pygame.sprite import Group
from typing_extensions import Self
from components.fish import Fish
from components.shark import Shark

colors = {
    'fish': pg.Color('#7ae843'),
    'shark': pg.Color('#e82233'),
    None: pg.Color('#42c4e5')
}

class Cell(Group):
    def __init__(self, type: (Fish | Shark | None), images, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.images = images
        
        self.background = pg.sprite.Sprite(self)
        self.background.image = pg.Surface((width, height))
        self.background.rect = pg.Rect(x, y, width, height)
        
        self.currentElement = None

        self.setType(type)
        

    def setType(self, type: (Fish | Shark | None)):
        self.type = type
        self.background.image.fill(colors[self.type])

        test = False
        if self.currentElement != None:
            self.currentElement.kill()
            test = True

        self.currentElement = None

        if test == False:
            if(type == 'fish'):
                self.currentElement = Fish(self, self.images[type], self.x, self.y, self.width, self.height)

            if(type == 'shark'):
                self.currentElement = Shark(self, self.images[type], self.x, self.y, self.width, self.height)
        
        if self.sprites() and test:
           for s in self.sprites():
                print(s)

