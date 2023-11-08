import pygame as pg
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

NB_COLS = 10
NB_ROWS = 10
NB_SHARK = 15
NB_FISH = 50

def imgs():
    return {
        'fish': pg.image.load(os.path.join('assets', 'poisson.png')).convert_alpha(),
        'shark': pg.image.load(os.path.join('assets', 'requin.png')).convert_alpha()
    }