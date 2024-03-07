#Canny Edge dector is a multi edge detection operator that uses a multi stage algorithm to detect a wide range of edges in images.
'''#
Canny edge detection algorithm is composed of 5 steps:
1. Noise reduction using gausian filter
2.Intensity Gradient calculation
3.Apply non-maximum suppression to get rid of spurious response to edge detetion
4.Apply Double Threshold to determine the potential edges
5.Edge tracking and hysteresis to finalise the detection of the edges by suppressing all the other edges that are weak or not connecting to strong edges
#'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
   pass
cv2.namedWindow('images')
img = cv2.imread('data/messi5.jpg',0)
canny = cv2.Canny(img,120,200)
titles = ['image','canny']
images =  [img,canny]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
#can = '100-200'
cv2.createTrackbar('100-200','images',100,400,nothing)

while(1):
    img1 =  cv2.imread('data/messi5.jpg')
    c= cv2.getTrackbarPos('100-200','images')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img1,str(c),(50,150),font,4,(0,0,255))
    cann = cv2.Canny(img1,c,200)
    print(c)
    cv2.imshow('images',cann)
    cv2.waitKey(0)
cv2.destroyAllWindows()
