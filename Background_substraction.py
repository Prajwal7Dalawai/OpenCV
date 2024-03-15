import numpy as np
import cv2
cap = cv2.VideoCapture('data/vtest.avi')
#kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while True:
    ret,frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
    cv2.imshow('Frame',frame)
    cv2.imshow('FG Maskframe',fgmask)
    k = cv2.waitKey(30)
    if k==ord('q') or 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
