import numpy as np
import cv2
'''#events = [i for i in dir(cv2) if 'EVENT_MOUSE' in i]
print(events)#'''


def click_event(event,x,y,flags,parameter):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_PLAIN
        strXY = str(x) + ',' + str(y)
        cv2.putText(img,strXY,(x,y),font,1,(255,255,0),1)
        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]    #these three lines red,green,blue identifies what colour is present on the specefic click on an image
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_PLAIN
        strbgr = str(blue) + ',' + str(green)+','+str(red)
        cv2.putText(img,strbgr,(x,y),font,1,(0,255,255),1)
        cv2.imshow('image',img)


img = cv2.imread('data/lena.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)     #this triggers a callback function whenever the mouse is clicked on
cv2.waitKey(0)
cv2.destroyAllWindows()