import os
import tifffile as tf
import Tkinter as Tk
import tkFileDialog


DIR_FORMAT = 'raw/channels8'


def split(fpath, destination):
    """
    Splits a TIFF stack into individual images, and outputs them to
    destination. The naming format is according to NeuroData specs,
    with images named in numerical order from '0000' to 'X'.

    :param fpath: File path of TIFF stack to split (eg a153_hs3)
    :param destination: Destination file path; default is location
                        of stack

    :type fpath: str
    :type destination: str


    :rtype None
    """
    image = tf.TiffFile(fpath)
    for i in range(len(image.pages)):
        if not os.path.exists(destination):
            os.makedirs(destination)
        tf.imsave("{0}/{1:04d}.tif".format(
            destination, i),
            image.pages[i].asarray())


def main():
    root = Tk.Tk()
    root.withdraw()
    start_dir = os.path.expanduser('~/Desktop/')
    cd = tkFileDialog.askdirectory(
        initialdir=start_dir)
    filepath = start_dir + '/' + os.path.basename(cd)
    hstackname = os.path.dirname(filepath)
    filepath += '/' + DIR_FORMAT
    time = 0
    for item in os.listdir(filepath):
        if item.endswith("ch1.tif"):
            path = '{0}/{1}'.format(filepath, item)
            split(path, '{0}/Channel/time{1}'.format(cd, time))
            print "Creating {0}: time{1}".format(hstackname, time)
            time += 1

if __name__ == '__main__':
    main()
