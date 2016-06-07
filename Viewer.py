import pygame as pg
import tiffstack as ts


class Viewer:
    def __init__(self, stack, caption="Stack Browser"):
        pg.init()
        pg.display.set_mode(pg.display.list_modes()[0], pg.RESIZABLE)
        pg.display.set_caption(caption)
        self.stack = stack
        self.screen = pg.display.get_surface()

        imarray = self.stack.getarray
        sz_to_use = tuple([imarray.shape[1], imarray.shape[2]])
        if self.screen.get_size() != sz_to_use:
            pg.display.set_mode(sz_to_use, 0, 8)
            pg.display.flip()
        pg.surfarray.blit_array(self.screen, imarray[0])


if __name__ == '__main__':
    t = ts.TiffStack("C:\Users\Chris\Desktop\Vascular-Data\X20140523_a153_001_ch2.tif")
    Viewer(t)
