import pygame as pg

def setup():

    clock = pg.time.Clock()

    fps = 30

    background = pg.image.load('assets/whiteBackground.png')
    
    canvas = pg.display.set_mode((background.get_width(), background.get_height()))

    return canvas, background,clock, fps
