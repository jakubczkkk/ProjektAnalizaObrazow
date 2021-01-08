from skimage import io
from skimage import color
from skimage import morphology
from skimage import transform
from skimage.filters import threshold_otsu
import numpy as np

def load_image(file_name):

    kitku = color.rgb2gray(io.imread(file_name))
    kitku = transform.resize(kitku, (300, 300))

    thresh = threshold_otsu(kitku)
    kitku = kitku > thresh

    kitku = morphology.binary_erosion(kitku)
    kitku = morphology.binary_dilation(kitku)

    kitku = morphology.remove_small_objects(kitku, min_size=50)
    kitku = morphology.remove_small_holes(kitku, area_threshold=50)

    io.imshow(kitku)
    io.show()
