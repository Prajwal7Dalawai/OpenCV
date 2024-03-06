#Homogeneous filter is the most simple filter, wach output pixel is the mean of its neighbours.
#In image processing, a kernel, convolution matrix, or a mask is a small matrix. It is used flor blurring, shapening, embossing,edge detction and more
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#img = cv.imread('data/opencv-logo.png')
img = cv.imread('data/lena.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
kernel = np.ones((5,5),np.float32)/25 
dst = cv.filter2D(img,-1,kernel) #cv.filter2D(name, desired depth of pirticular image, kernal)

#As in one dimensional signals, images also can be filtered with various low pass filters(LPF), high-pass filters(HPF),etc
#Low class filters helps in removing noise,
#high class filters helps in removing edges

blur = cv.blur(img,(5,5))

#gausiing filter is nothing but usinf different-weight-kernel, in both x and y direction

gblur = cv.GaussianBlur(img,(5,5),0)

#Median filter is something that replace each pixel's value with the median of its neighbouring pixels. This method is great when dealing with "Salt and pepper noise"
median = cv.medianBlur(img,5)
bilateralfilter = cv.bilateralFilter(img,9,75,75) # this filter very helpful in noise removal by keeping the edge sharp

titles = ['image','dest','blur','gblur','median','Bilateral filter']
images = [img,dst,blur,gblur,median,bilateralfilter]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()