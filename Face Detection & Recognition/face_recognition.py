import cv2
import numpy as np
cap = cv2.VideoCapture(0)
face_cascade - cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv2.imshow('frame',frame)
        k= cv2.waitKey(1)
        if k == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()