import pygame as pg


class Tile(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.placed = False
        self.image = pg.image.load("sprite/tile").convert_alpha()  # le chemin est a change

    def move_side(self, direction):
        self.x += direction

    def move_down(self):
        self.y += 1

    def draw(self):
        ...