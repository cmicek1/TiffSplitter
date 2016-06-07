import os
import tifffile as tf
import Tkinter as Tk
import tkFileDialog


class TiffSplitter:
    """
    Utility for splitting 3D TIFF files into individual TIFF images.
    Meant for use with the Open Connectome Project's NeuroDataViz tool.
    """
    def __init__(self, location):
        """
        Constructor; creates splitting utility.

        :param location: directory path of TIFF stacks to split

        :type location: str
        :type destination: str
        """
        self.location = location

    def split(self, fpath, destination):
        """
        Splits a TIFF stack into individual images, and outputs them to
        destination. The naming format is according to NeuroData specs,
        with images named in numerical order from '0000' to 'X'.

        :param fpath: file path of TIFF stack to split
        :param destination: destination file path; default is location
                            of stack

        :type fpath: str
        :type destination: str

        :rtype: None
        """
        image = tf.TiffFile(fpath)
        for i in range(len(image.pages)):
            if not os.path.exists(destination):
                os.makedirs(destination)
            tf.imsave("{0}/{1:04d}.tif".format(
                destination, i),
                image.pages[i].asarray())


if __name__ == "__main__":
    root = Tk.Tk()
    root.withdraw()
    cd = tkFileDialog.askdirectory()
    ts = TiffSplitter(cd)
    for item in os.listdir(ts.location):
        if item.endswith(".tif"):
            path = "{0}/{1}".format(ts.location, item)
            ts.split(path, path.split(".")[0])
