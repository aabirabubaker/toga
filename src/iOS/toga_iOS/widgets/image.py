from ..libs import *


class Image(object):
    def __init__(self, interface):
        self.interface = interface
        self.interface._impl = self

    def load_image(self, path):
        if path.startswith('http://') or path.startswith('https://'):
            self.native = UIImage.imageWithData_(NSData.dataWithContentsOfURL_(NSURL.URLWithString_(path)))
        else:
            self.native = UIImage.alloc().initWithContentsOfFile_(path)
