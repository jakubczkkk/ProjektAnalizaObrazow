# coś z konturami

# import numpy as np
# import matplotlib.pyplot as plt

# from skimage import measure


# # Construct some test data
# x, y = np.ogrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]
# r = np.sin(np.exp((np.sin(x)**3 + np.cos(y)**2)))

# # Find contours at a constant value of 0.8
# contours = measure.find_contours(r, 0.8)

# # Display the image and plot all contours found
# fig, ax = plt.subplots()
# ax.imshow(r, cmap=plt.cm.gray)

# for contour in contours:
#     ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

# ax.axis('image')
# ax.set_xticks([])
# ax.set_yticks([])
# plt.show()


# coś innego z konturami

# import cv2 
# import numpy as np 
  
# # Let's load a simple image with 3 black squares 
# image = cv2.imread("images/training/cats/cat.2.jpg") 
# cv2.waitKey(0) 
  
# # Grayscale 
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
# # Find Canny edges 
# edged = cv2.Canny(gray, 30, 200) 
# cv2.waitKey(0) 
  
# # Finding Contours 
# # Use a copy of the image e.g. edged.copy() 
# # since findContours alters the image 
# contours, hierarchy = cv2.findContours(edged,  
#     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
# cv2.imshow('Canny Edges After Contouring', edged) 
# cv2.waitKey(0) 
  
# print("Number of Contours found = " + str(len(contours))) 
  
# # Draw all contours 
# # -1 signifies drawing all contours 
# cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
  
# cv2.imshow('Contours', image) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows() 


# import cv2
# import numpy as np

# img = cv2.imread("images/training/cats/cat.2.jpg", cv2.IMREAD_UNCHANGED)

# #convert img to grey
# img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #set a thresh
# thresh = 100
# #get threshold image
# ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)
# #find contours
# contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# #create an empty image for contours
# img_contours = np.zeros(img.shape)
# # draw the contours on the empty image
# cv2.drawContours(img_contours, contours, -1, (0,255,0), 3)
# cv2.imshow('Contours', img_contours) 
# #save image
# cv2.imwrite("images/cat.2.png",img_contours) 

import numpy as np
import matplotlib.pyplot as plt

from skimage.filters import sobel
from skimage.measure import label
from skimage.segmentation import watershed, expand_labels
from skimage.color import label2rgb
from skimage import data
#
from skimage import io
import os
from skimage import data, filters

# coins = data.coins()
filename = os.path.join(skimage.data_dir, "images/training/cats/cat.1.jpg")

coins = io.imread(filename) # coins to image
# coins = io.imread("images/training/cats/cat.1.jpg")#image
# Make segmentation using edge-detection and watershed.
# edges = sobel(coins)
edges = filters.sobel(coins)

# Identify some background and foreground pixels from the intensity values.
# These pixels are used as seeds for watershed.
markers = np.zeros_like(coins)
foreground, background = 1, 2
markers[coins < 30.0] = background
markers[coins > 150.0] = foreground

ws = watershed(edges, markers)
seg1 = label(ws == foreground)

expanded = expand_labels(seg1, distance=10)

# Show the segmentations.
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 5),
                         sharex=True, sharey=True)

color1 = label2rgb(seg1, image=coins, bg_label=0)
axes[0].imshow(color1)
axes[0].set_title('Sobel+Watershed')

color2 = label2rgb(expanded, image=coins, bg_label=0)
axes[1].imshow(color2)
axes[1].set_title('Expanded labels')

for a in axes:
    a.axis('off')
fig.tight_layout()
plt.show()