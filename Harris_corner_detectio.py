'''#Haris Corner Detector
1.Determine which windows produce very large variations in intensity when moved in both X and Y directions.
2.With each such window found, a score R is computed.
3.After applying a threshold to this score, important corners are selected and marked.
#'''
import numpy as np
import cv2 
img = cv2.imread('data/chessboard.png')
cv2.imshow('chess',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
img[dst>0.01*dst.max()] = [0,0,255]
cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindows()