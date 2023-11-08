import pygame as pg

from components.world import World
from constants import *

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #, pg.RESIZABLE)

    clock = pg.time.Clock()
    running = True

    w = World(screen, imgs(), width=screen.get_width(), height=screen.get_height()) 

    while running:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for i, cell in enumerate(w.flatCells):
                    if cell.rect.collidepoint(event.pos):
                        cell.onClick(event)

            if event.type == pg.QUIT:
                running = False
        
        w.update()
        pg.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    main()
    pg.quit()