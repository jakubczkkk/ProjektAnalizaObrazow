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

    binarized_cat = process_image(file_name)
    io.imshow(binarized_cat)
    io.show()


def process_image(file_name):

    cat = color.rgb2gray(io.imread(file_name))
    cat = transform.resize(cat, (300, 300))

    # thresh = threshold_otsu(cat)
    # cat = cat > thresh

    # cat = morphology.binary_erosion(cat)
    # cat = morphology.binary_dilation(cat)

    # cat = morphology.remove_small_objects(cat, min_size=50)
    # cat = morphology.remove_small_holes(cat, area_threshold=50)

    return cat.flatten()


def training_animals(animal):

    data = []

    for i in range(1, 101):
        file_name = f"images/training/{animal}s/{animal}.{i}.jpg"

        new_animal = process_image(file_name)

        data.append(new_animal)

    return data

