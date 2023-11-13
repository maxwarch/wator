import pygame as pg

from components.world import World
from constants import *

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.DOUBLEBUF, 8) #, pg.RESIZABLE)

    clock = pg.time.Clock()
    running = True

    w = World(screen, imgs(), width=screen.get_width(), height=screen.get_height()) 
    pg.event.set_allowed([pg.QUIT, pg.KEYDOWN])
    
    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    w.update()

            if event.type == pg.MOUSEBUTTONDOWN:
                for i, cell in enumerate(w.flatCells):
                    if cell.rect.collidepoint(event.pos):
                        cell.onClick(event)

            if event.type == pg.QUIT:
                running = False
        
        pg.display.flip()

        clock.tick(60)

        pg.event.pump()
        pg.time.delay(30)
        w.update()
        #print(clock.get_fps())

if __name__ == '__main__':
    main()
    pg.quit()