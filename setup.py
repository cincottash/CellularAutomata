import pygame as pg
import sys

def setup():

    clock = pg.time.Clock()

    fps = 60
    
    width = height = int(sys.argv[1])
    
    canvas = pg.display.set_mode((width, height))

    return canvas, clock, fps
