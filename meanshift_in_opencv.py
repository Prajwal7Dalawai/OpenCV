import numpy as np
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture('data/traffic.webm')

#1.Take the first frame of the window.
ret, frame = cap.read()

#2.Set up the initial location of window.
x,y,width,hieght = 300,200,100,50
track_window = (x,y,width,hieght)

#3.Set up the ROI of tracking
roi = frame[y:y+hieght,x:x+width]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((0.,60.,32.,)),np.array((180.,255.,255.,)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
#4.Set up the termination criteria, either 10 iteration or move by one point.
term_crit = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10,1)

while(1):
        ret, frame = cap.read()
        if ret == True:
            hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
            #apply meanshift to get new position
            #ret,track_window = cv2.meanShift(dst,track_window,term_crit)
            ret,track_window = cv2.CamShift(dst,track_window,term_crit)
            #draw it on a image
            x,y,w,h = track_window
            final_image = cv2.rectangle(frame,(x,y),(x+w,y+h),255,3)
            cv2.imshow('frame',frame)
            cv2.imshow('final frame',final_image)
            cv2.imshow('dst',dst)
            k =  cv2.waitKey(30) and 0xff
            if k == ord('q'):
                break
        else:
             break
cap.release()  #Release all the captured resources
cv2.destroyAllWindows()
