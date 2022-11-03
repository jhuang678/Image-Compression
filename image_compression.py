######################################################################
import math
import time
import copy
import pandas as pd
import seaborn as sns
import scipy.io as sio

import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import ImageCompressor as ic
from matplotlib.pyplot import imshow
from itertools import combinations
from PIL import Image
from scipy.sparse import csc_matrix, find

#####################################################################

if __name__ == '__main__':

    compressor = ic.ImageCompressor(verbose=True)
    compressor.read_bmp(bmp_path = "wdw.bmp", img_path = "wdw_array.png")
    compressor.kmeans_compress(k=2, norm=2, img_path="wdw_compressed_k_2.png")
    compressor.kmeans_compress(k=3, norm=2, img_path="wdw_compressed_k_3.png")
    compressor.kmeans_compress(k=4, norm=2, img_path="wdw_compressed_k_4.png")
    compressor.kmeans_compress(k=5, norm=2, img_path="wdw_compressed_k_5.png")

    print("Done!")

