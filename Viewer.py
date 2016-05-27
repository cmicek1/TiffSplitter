import pygame as pg
import numpy as np
import TiffStack as ts

class Viewer:
    def __init__(self, stack, caption="Stack Browser"):
        pg.init()
        pg.display.set_mode(pg.display.list_modes()[0], pg.RESIZABLE)
        pg.display.set_caption(caption)
        self.stack = stack

        imarray = self.stack.image.asarray()
        pg.surfarray.blit_array(pg.display.get_surface(), imarray[1])



