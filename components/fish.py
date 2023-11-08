from pygame.sprite import Sprite
import pygame as pg


class Fish(Sprite):
    def __init__(self, groups, image, position, size):
        super().__init__(groups)
        percent = 80
        scaled = (percent * size[0])/100 if size[0] < size[1] else (percent * size[1])/100
        image = pg.transform.smoothscale(image, (scaled, scaled))
        self.image = image
        self.rect = self.image.get_rect(center = (position[0] + size[0] / 2, position[1] + size[1] / 2))