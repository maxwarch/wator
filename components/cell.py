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
    def __init__(self, screen, type: (Fish | Shark | None), images, position, size):
        super().__init__()

        self.screen = screen
        self.size = size
        self.position = position
        self.images = images
        
        self.background = pg.sprite.Sprite(self)
        self.background.image = pg.Surface(size)
        self.background.rect = pg.Rect(position, size)
        
        self.currentElement = None

        self.setType(type)
        

    def setType(self, type: (Fish | Shark | None)):
        self.type = type
        self.background.image.fill(colors[self.type])

        if self.currentElement != None:
            self.currentElement.kill()

        self.currentElement = None

        if(type == 'fish'):
            self.currentElement = Fish(self, self.images[type], self.position, self.size)

        if(type == 'shark'):
            self.currentElement = Shark(self, self.images[type], self.position, self.size)

        self.render()

    def render(self):
        self.update()
        self.draw(self.screen)
