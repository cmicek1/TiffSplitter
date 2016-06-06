import os
import tifffile as tf
import Tkinter as Tk
import tkFileDialog


class TiffSplitter:
    """
    Utility for splitting 3D TIFF files into individual TIFF images.
    Meant for use with the Open Connectome Project's NeuroDataViz tool.
    """
    def __init__(self, location, destination=None):
        """
        Constructor; creates splitting utility.

        :param location: file path of TIFF stack to split
        :param destination: destination file path; default is location
                            of stack
        :type location: str
        :type destination: str
        """
        self.location = location
        if destination is None:
            self.destination = self.location
        else:
            self.destination = destination

    def split(self):
        """
        Splits a TIFF stack into individual images, and outputs them to
        destination. The naming format is according to NeuroData specs,
        with images named in numerical order from '0000' to 'X'.
        :rtype: None
        """
        image = tf.TiffFile(self.location)
        for i in range(len(image.pages)):
            tf.imsave("{0}\{1:04d}.tif".format(
                os.path.dirname(self.location), i), image.pages[i].asarray())


if __name__ == "__main__":
    root = Tk.Tk()
    root.withdraw()
    fpath = tkFileDialog.askopenfilename()
    ts = TiffSplitter(fpath)
    ts.split()
