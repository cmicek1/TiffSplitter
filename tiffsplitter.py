import tifffile as tf
import Tkinter as tk
import tkFileDialog


class TiffSplitter:
    def __init__(self, location, destination=None):
        """

        :type destination: str
        """
        self.location = location
        if destination is None:
            self.destination = self.location
        else:
            self.destination = destination

    def split(self):
        image = tf.TiffFile(self.location)
        for i in range(len(image.pages)):
            tf.imsave("{0}_{1}.tif".format(self.destination.split(".tif")[0], str(i)), image.pages[i].asarray())


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    fpath = tkFileDialog.askopenfilename()
    ts = TiffSplitter(fpath)
    ts.split()
