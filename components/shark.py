from random import randint
import pygame as pg

from components.fish import Fish
from constants import NB_CHRONON_FISH_PREGNANCY, NB_CHRONON_SHARK_ENERGY, NB_CHRONON_SHARK_PREGNANCY


class Shark(Fish):
    def __init__(self, group, image, position, size):
        super().__init__(group, image, position, size)

    def init(self):
        self.setParams(pregnancy=NB_CHRONON_SHARK_PREGNANCY, energy=NB_CHRONON_SHARK_ENERGY)
    
    def moveRules(self, cellsAround):
        fishCells = [cell for cell in cellsAround if cell.type == 'fish']
        if len(fishCells) > 0:
            self.params['energy'] += 1
            return fishCells[randint(0, len(fishCells) - 1)]
        
        emptyCells = [cell for cell in cellsAround if cell.type == None]
        if len(emptyCells) > 0:
            return emptyCells[randint(0, len(emptyCells) - 1)]
            
        return None
    
    def setEnergy(self):
        self.params['energy'] -= 1

        result = self.params['energy'] > 0
        if result == False:
            self.setParams(energy=NB_CHRONON_SHARK_ENERGY)

        return result

    def doReproduce(self, pregnancy=...):
        return super().doReproduce(NB_CHRONON_SHARK_PREGNANCY)