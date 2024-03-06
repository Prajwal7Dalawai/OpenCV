#thresholding is a process of comparing each pixels of the image to the threshold value, divides all the values of the inputs into two 
#groups:- first groups: Pixels having lower than threshold values, second group: pixels having higher value threshold value
import cv2 as cv
import numpy as np
img = cv.imread('data/gradient.png',0)
_ , th1 = cv.threshold(img,50,255,cv.THRESH_BINARY) #Gives lower value until the threshold value, gives maximum value after threshold value
_ , th2 = cv.threshold(img,50,255,cv.THRESH_BINARY_INV) #inverse of THRESH_BINARY
_ , th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC) #Doesn't change any value until threshold value, after the threshold value the value of all pixel will be threshold value
_ , th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)    #Value below the threshold value is minimum, after the threshold value the value of all pixel will be threshold value
_ , th5 = cv.threshold(img,50,255,cv.THRESH_TOZERO_INV) #inverse of THRESH_TOZERO
cv.imshow("Image",img)  
cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('th4',th4)
cv.imshow('th5',th5)
cv.waitKey(0)
cv.destroyAllWindows()