from skimage import io
from skimage import color
from skimage import morphology
from skimage import transform
from skimage.filters import threshold_otsu
from skimage import filters

import scipy.ndimage as nd
import numpy as np
import matplotlib.pyplot as plt

import customfilters as fltrs

def invert_binary_colors(image):
    inverted_image = image
    for i in range(len(image)):
        for j in range(len(image[0])):
            inverted_image[i][j] = not image[i][j]
    return inverted_image

def convolve(image, mask):
    convolved = image
    nd.convolve(image, mask, convolved)
    return convolved


def load_image(file_name):

    kitku = io.imread(file_name)
    kitku = color.rgb2gray(io.imread(file_name))
    
    kitku = transform.resize(kitku, (300, 300))

    thresh = threshold_otsu(kitku)
    kitku = kitku > thresh
    
    kitku = morphology.binary_erosion(kitku)
    kitku = morphology.binary_dilation(kitku)

    kitku = morphology.remove_small_objects(kitku, min_size=50)
    kitku = morphology.remove_small_holes(kitku, area_threshold=50)

    plt.imshow(kitku, cmap='gray')
    plt.show()


load_image('testImages/kitku5.png')