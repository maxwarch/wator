from pygame.sprite import Sprite
import pygame as pg


class Fish(Sprite):
    def __init__(self, group, image, x, y, width, height):
        super().__init__(group)
        percent = 80
        size = (percent * width)/100 if width < height else (percent * height)/100
        image = pg.transform.smoothscale(image, (size, size))
        self.image = image
        self.rect = self.image.get_rect(center = (x + width / 2, y + height / 2))