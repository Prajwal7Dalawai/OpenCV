import numpy as np
import cv2
cap = cv2.VideoCapture('data/traffic.webm')
'''#
1.Take the first frame of the window.
2.Set up the initial location of window.
3.Set up the ROI of tracking
4.Set up the termination criteria, either 10 iteration or move by one point.
#'''
while(1):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame',frame)
            k =  cv2.waitKey(30) and 0xff
            if k == ord('q'):
                break
        else:
             break
cap.release()  #Release all the captured resources
cv2.destroyAllWindows()
