import numpy as np
import cv2
img = cv2.imread('data/pic5.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()