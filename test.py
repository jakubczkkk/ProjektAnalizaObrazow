# from skimage.util import img_as_float
from skimage import io
from skimage import color
from skimage import morphology
from skimage import transform
from skimage.filters import threshold_otsu
import numpy as np

kitku = color.rgb2gray(io.imread("kitku2.jpg"))
kitku = transform.resize(kitku, (300, 300))

thresh = threshold_otsu(kitku)
kitku = kitku > thresh

kitku = morphology.erosion(kitku)
kitku = morphology.dilation(kitku)

io.imshow(kitku)
io.show()
