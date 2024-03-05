import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
def nothing(x):
    print(x)
cv2.createTrackbar('B','image',0,255,nothing)  # creation of trackbar arguments: name of trackbar, name of window, intial value, final value, callback function
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)
switch = '0: off\n1: On'
cv2.createTrackbar('switch','image',0,1,nothing)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')
    swi = cv2.getTrackbarPos('switch','image')
    if swi == 0:
        img[ : ] = 0
    else:
        img[ : ] = [b, g, r]
cv2.destroyAllWindows()