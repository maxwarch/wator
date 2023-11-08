from array import array
from operator import itemgetter
import random
import pygame as pg
from components.cell import Cell

class World:
    def __init__(self, screen, images, **kwargs):
        self.screen = screen
        self.images = images

        self.options = {
                'nbFish' : 50,
                'nbShark' : 15,
                'width': 800, 
                'height': 600,
                'nbRows': 10, 
                'nbCols': 10
            }

        self.options.update(kwargs)

        self.initWorld = self.init()

    def init(self) -> array:
        nbRows, nbCols, nbFish, nbShark = itemgetter('nbRows', 'nbCols', 'nbFish', 'nbShark')(self.options)
        elements = ['fish' for i in range(nbFish)] + ['shark' for i in range(nbShark)]
        cases = [None]*((nbRows * nbCols) - len(elements)) + elements
        cases = random.sample(list(cases), len(cases))
        
        return cases

    def render(self):
        nbRows, nbCols, width, height = itemgetter('nbRows', 'nbCols', 'width', 'height')(self.options)
        self.cellSize = (int(width / nbRows), int(height / nbCols))

        self.mesh = []

        index = 0
        for row in range(0, nbRows):
            self.mesh.append([])
            for col in range(0, nbCols):
                cell = Cell(self.screen, self.initWorld[index], self.images, (col * self.cellSize[0], row * self.cellSize[1]), (self.cellSize[0] - 2, self.cellSize[1] - 2))
                self.mesh[row].append(cell)
                index += 1

        return self.mesh
    
    def change(self):
        cell = self.mesh[0][0]
        cell.setType('shark')

    def update(self):
        pass
