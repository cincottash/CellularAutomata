import pygame as pg
import sys

def setup():

    clock = pg.time.Clock()

    fps = 30
    
    width = height = int(sys.argv[1])
    
    canvas = pg.display.set_mode((width, height))

    return canvas, clock, fps
