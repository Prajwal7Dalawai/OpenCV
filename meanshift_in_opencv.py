import numpy as np
import cv2
cap = cv2.VideoCapture('data/traffic.webm')
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
