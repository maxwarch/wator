import pygame as pg
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60

NB_COLS = 50
NB_ROWS = 50
NB_SHARK = 20
NB_FISH = 200
NB_CHRONON_FISH_PREGNANCY = 2
NB_CHRONON_SHARK_PREGNANCY = 10
NB_CHRONON_SHARK_ENERGY = 3

def imgs():
    return {
        'fish': pg.image.load(os.path.join('assets', 'poisson.png')).convert_alpha(),
        'shark': pg.image.load(os.path.join('assets', 'requin.png')).convert_alpha()
    }