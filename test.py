from skimage import io
from skimage import color
from skimage import morphology
from skimage import transform
from skimage.filters import threshold_otsu
import numpy as np

from skimage import data, filters

def load_image(file_name):

    binarized_cat = process_image(file_name)
    io.imshow(binarized_cat)
    io.show()


def process_image(file_name):

    cat = color.rgb2gray(io.imread(file_name))
    cat = transform.resize(cat, (300, 300))

    thresh = threshold_otsu(cat)
    cat = cat > thresh

    cat = morphology.binary_erosion(cat)
    cat = morphology.binary_dilation(cat)

    cat = morphology.remove_small_objects(cat, min_size=50)
    cat = morphology.remove_small_holes(cat, area_threshold=50)

    return cat


def training_animals(animal, start=1, stop=500):

    data = []

    for i in range(1, 501):
        file_name = f"images/training/{animal}s/{animal}.{i}.jpg"

        new_animal = process_image(file_name)

        data.append(new_animal)

    return data

def test_animals(start=1, stop=500):

    data = []
    animal = "cat"
    for i in range(1, 501):
        file_name = f"images/training/{animal}s/{animal}.{i}.jpg"

        new_animal = process_image(file_name)

        data.append(new_animal)
    
    animal = "dog"
    for i in range(1, 501):
        file_name = f"images/training/{animal}s/{animal}.{i}.jpg"

        new_animal = process_image(file_name)

        data.append(new_animal)

    return data

image = io.imread("images/training/cats/cat.5.jpg")
# image = load_image("images/training/cats/cat.1.jpg")

edges = filters.sobel(image)
io.imshow(edges)
io.show()


# io.imshow(image)
# io.show()