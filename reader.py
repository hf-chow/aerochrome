import rawpy
import imageio

def read_raw(path):
    with rawpy.imread(path) as raw:
        rgb = raw.postprocess()

def get_channels(path):
    pass

