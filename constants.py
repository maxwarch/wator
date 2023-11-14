import pygame as pg
import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
FPS = 60
REFRESH_DELAY=30 #ms

NB_COLS = 80
NB_ROWS = 80
NB_SHARK = 300
NB_FISH = 600
NB_CHRONON_FISH_PREGNANCY = 2
NB_CHRONON_SHARK_PREGNANCY = 10
NB_CHRONON_SHARK_ENERGY = 4

def imgs():
    return {
        'fish': pg.image.load(os.path.join('assets', 'poisson.png')).convert_alpha(),
        'shark': pg.image.load(os.path.join('assets', 'requin.png')).convert_alpha()
    }