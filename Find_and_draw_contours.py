#Contours are the curves joining all the continous point along the boundary having same color and intensity, it use useful for 
#object detection, shape analysis or object recognition
import cv2
import numpy as np
img = cv2.imread('data/opencv-logo.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,tresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(tresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#Here contour variable is the python list of all the contours in the image. Each individual contour is a numpy array of (x,y) co-ordinates
#of boundary points of the object
print(" Number of Contours = " + str(len(contours)))
print(contours[0])
cv2.drawContours(img,contours,-1,(90,200,190),3)
cv2.imshow('Image',img)
#cv2.imshow('Image Gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()