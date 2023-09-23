import pygame as pg


class Tile(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.position = ...
        self.placed = False
        self.image = pg.image.load("sprite/tile").convert_alpha()  # le chemin est a change

    def move_right(self):
        ...

    def move_left(self):
        ...

    def move_down(self):
        ...
