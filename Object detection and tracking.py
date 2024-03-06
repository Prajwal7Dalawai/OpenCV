import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("tracking")

while True:
    frame = cv2.imread('data/smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #Converting to HSV colour

    l_b = np.array([110, 50, 50]) #lower base colour blue
    u_b = np.array([130, 255, 255]) #higher base colour blue
    
    mask = cv2.inRange(hsv, l_b, u_b)   #creating the mask of the image
    ress = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', ress) 
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
