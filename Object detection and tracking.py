import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("tracking")

while True:
    frame = cv2.imread('data/smarties.png')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Fix: Convert to HSV instead of GRAY

    l_b = np.array([110, 50, 50])
    u_b = np.array([130, 255, 255])
    
    mask = cv2.inRange(hsv, l_b, u_b)
    ress = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', ress)  # Fix: Correct the function name to cv2.imshow
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
