#Morphological operations are simple operations performed on binary image based on image shape.
#A kernel tells you how to change the value of any given pixel by combining it with different amounts of the neighbouring pixels
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('data/smarties.png',0)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal = np.ones((2,2),np.uint8) # kernal is a square or a shape which we want to apply on the image
dilation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=1)
open = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
close = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
titles = ['image','mask','dilation','erosion','open','close']
images = [img,mask,dilation,erosion,open,close]

for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()