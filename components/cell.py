from typing import List
from typing_extensions import Self
import pygame as pg
from typing_extensions import AnyStr
from pygame.sprite import Group
from components.fish import Fish
from components.shark import Shark

colors = {
    'fish': pg.Color('#7ae843'),
    'shark': pg.Color('#e82233'),
    None: pg.Color('#42c4e5'),
    'other': 'yellow'
}

class Cell(Group):
    def __init__(self, screen, type: (Fish | Shark | None), images, coord, position, size, cbMove):
        super().__init__()

        self.coord = coord
        self.screen = screen
        self.size = size
        self.position = position
        self.images = images
        self.type = type
        self.cbMove = cbMove
        self.currentElement = None
        self.dirty = False
        
        self.background = pg.sprite.Sprite(self)
        self.background.image = pg.Surface(size)
        self.rect = self.background.rect = pg.Rect(position, size)

        self.elements = {
            'fish': Fish(self, images['fish'], self.position, self.size),
            'shark': Shark(self, images['shark'], self.position, self.size)
        }

        self.setType(type)

    def setType(self, type: AnyStr | None, params = None):
        self.type = type
        self.background.image.fill(colors[self.type])

        if self.currentElement != None:
            self.currentElement.hide()

        self.currentElement = None

        if type != None:
            self.currentElement = self.elements[self.type]
            self.currentElement.show()
            if params != None and params != 'new':
                self.currentElement.setParams(**params)

            if params == 'new':
                self.currentElement.init()
            

        self.render()

    def onUpdate(self, cellsAround: List[Self]):
        if self.currentElement == None:
            return None
        
        return (
            self.currentElement.moveRules(cellsAround),
            self.currentElement.doReproduce(),
            self.currentElement.setEnergy(),
            self.currentElement.getParams()
        )

    def onClick(self, event):
        if self.type == 'fish' or self.type == None:
            self.setType('shark')
        else:
            self.setType('fish')

    def render(self):
        self.update()
        self.draw(self.screen)
