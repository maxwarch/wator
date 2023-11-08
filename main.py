import os
import pygame as pg

from components.world import World

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600)) #, pg.RESIZABLE)

    IMGS = {
        'fish': pg.image.load(os.path.join('assets', 'poisson.png')).convert_alpha(),
        'shark': pg.image.load(os.path.join('assets', 'requin.png')).convert_alpha()
    }

    clock = pg.time.Clock()
    running = True

    w = World(screen, IMGS, width=screen.get_width(), height=screen.get_height()) 
    w.render()

    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    w.change()

            if event.type == pg.QUIT:
                running = False
        
        w.update()
        pg.display.flip()

        clock.tick(60)

if __name__ == '__main__':
    main()
    pg.quit()