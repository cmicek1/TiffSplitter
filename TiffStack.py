import tifffile as tf
class TiffStack:
    def __init__(self, directory):
        self.directory = directory
        self.image = tf.TiffFile(self.directory)