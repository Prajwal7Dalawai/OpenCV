#Image gradient is the directional change in the intensity or colour in the image
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('data/sudoku.png',0)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3) #CV_64F is a float data type which supports -ve numbers
lap = np.uint8(np.absolute(lap))
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelcomb = cv2.bitwise_or(sobelx,sobely)
titles = ['image','laplacian','sobelX','sobelY','sobel combine']
images =  [img,lap,sobelx,sobely,sobelcomb]
for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()