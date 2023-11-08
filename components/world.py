from array import array
from operator import itemgetter
import random
from components.cell import Cell
from constants import *

class World:
    def __init__(self, screen, images, **kwargs):
        self.options = {
                'nbFish' : NB_FISH,
                'nbShark' : NB_SHARK,
                'width': SCREEN_WIDTH, 
                'height': SCREEN_HEIGHT,
                'nbRows': NB_ROWS, 
                'nbCols': NB_COLS
            }

        self.options.update(kwargs)

        self.initWorld = self.init()
        self.render(screen, images)

    def init(self) -> array:
        nbRows, nbCols, nbFish, nbShark = itemgetter('nbRows', 'nbCols', 'nbFish', 'nbShark')(self.options)
        elements = ['fish' for i in range(nbFish)] + ['shark' for i in range(nbShark)]
        cases = [None]*((nbRows * nbCols) - len(elements)) + elements
        cases = random.sample(list(cases), len(cases))
        
        return cases

    def render(self, screen, images):
        nbRows, nbCols, width, height = itemgetter('nbRows', 'nbCols', 'width', 'height')(self.options)
        self.cellSize = (int(width / nbRows), int(height / nbCols))

        self.cells = []

        index = 0
        for row in range(0, nbRows):
            self.cells.append([])
            for col in range(0, nbCols):
                cell = Cell(screen, self.initWorld[index], images, (col * self.cellSize[0], row * self.cellSize[1]), (self.cellSize[0] - 2, self.cellSize[1] - 2))
                self.cells[row].append(cell)
                index += 1

        self.flatCells = [item for row in self.cells for item in row]        

    def update(self):
        pass
