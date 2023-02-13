import os
import pygame
import sys


class Sp(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.image = self.load_image()
        self.rect = self.image.get_rect()

    def load_image(self, colorkey=None):
        fullname = os.path.join('data', self.name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

