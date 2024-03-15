import numpy as np
import cv2
cap = cv2.VideoCapture('data/vtest.avi')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while True:
    ret,frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    cv2.imshow('Frame',frame)
    cv2.imshow('FG Maskframe',fgmask)
    k = cv2.waitKey(30)
    if k==ord('q') or 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
