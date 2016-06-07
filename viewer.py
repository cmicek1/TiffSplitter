import pygame as pg
import tiffstack as ts
import Tkinter as Tk
import tkFileDialog

BIT_DEPTH = 8


class Viewer:
    def __init__(self, stack, caption="Stack Browser"):
        self.stack = stack
        pg.init()
        imarray = self.stack.getarray
        sz_to_use = tuple([imarray.shape[1], imarray.shape[2]])
        self.screen = pg.display.set_mode(sz_to_use, pg.RESIZABLE,
                                          BIT_DEPTH)
        pg.display.set_caption(caption)

        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        pg.surfarray.blit_array(self.background, imarray[20])
        self.screen.blit(self.background, (0, 0))
        pg.display.flip()


def main():
    root = Tk.Tk()
    root.withdraw()
    fpath = tkFileDialog.askopenfilename()
    t = ts.TiffStack(fpath)
    v = Viewer(t)
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                quit(0)

        v.screen.blit(v.background, (0, 0))
        pg.display.flip()


if __name__ == '__main__':
    main()
