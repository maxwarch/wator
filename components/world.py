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

        self.inited = False

        self.initWorld = self.init()
        self.render(screen, images)
        self.inited = True

    def init(self) -> array:
        nbRows, nbCols, nbFish, nbShark = itemgetter('nbRows', 'nbCols', 'nbFish', 'nbShark')(self.options)
        elements = ['fish' for i in range(nbFish)] + ['shark' for i in range(nbShark)]
        cases = [None]*((nbRows * nbCols) - len(elements)) + elements
        cases = random.sample(list(cases), len(cases))
        
        #print(cases)
        return cases

    def render(self, screen, images):
        nbRows, nbCols, width, height = itemgetter('nbRows', 'nbCols', 'width', 'height')(self.options)
        self.cellSize = (int(width / nbRows), int(height / nbCols))

        self.cells = []

        index = 0
        for row in range(0, nbRows):
            self.cells.append([])
            for col in range(0, nbCols):
                cell = Cell(screen, 
                            self.initWorld[index], 
                            images, 
                            coord=(row, col), 
                            position=(col * self.cellSize[0], row * self.cellSize[1]), 
                            size=(self.cellSize[0] - 2, self.cellSize[1] - 2),
                            cbMove = self.cellMove)
                self.cells[row].append(cell)
                index += 1
        self.flatCells = [item for row in self.cells for item in row]  

    def cellMove(self, cell: Cell):
        if self.inited == False:
            return
        
        row = cell.coord[0]
        col = cell.coord[1]

        nextCol = col + 1
        nextCol = 0 if nextCol >= NB_COLS else nextCol
        prevCol = col - 1
        prevCol = NB_COLS - 1 if prevCol < 0 else prevCol

        nextRow = row + 1
        nextRow = 0 if nextRow >= NB_ROWS else nextRow
        prevRow = row - 1
        prevRow = NB_ROWS - 1 if prevRow < 0 else prevRow

        cellsAround = [
            self.cells[row][nextCol],
            #self.cells[nextRow][nextCol],
            self.cells[nextRow][col],
            #self.cells[nextRow][prevCol],
            self.cells[row][prevCol],
            #self.cells[prevRow][prevCol],
            self.cells[prevRow][col],
            #self.cells[prevRow][nextCol],
        ]

        nextCell, reproduce, energy, params = cell.onUpdate(cellsAround)
        #print(params)
        if nextCell != None:
            cellType = cell.type

            if energy == False:
                cell.setType(None)
            else:
                nextCell.setType(cellType, params)
                cell.setType(None)

                if reproduce:
                    cell.setType(cellType, 'new')

                nextCell.dirty = True

    def update(self):
        for cell in self.flatCells:
            if (cell.type == 'fish' or cell.type == 'shark') and cell.dirty == False:
                self.cellMove(cell)

        def initDirty(cell: Cell):
            cell.dirty = False
            return cell
        
        self.flatCells = list(map(initDirty, self.flatCells))