import numpy as np
import cv2
'''#events = [i for i in dir(cv2) if 'EVENT_MOUSE' in i]
print(events)#'''


def click_event(event,x,y,flags,parameter):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,(points[-1]),(points[-2]),(255,0,0),5)
    cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]    #these three lines red,green,blue identifies what colour is present on the specefic click on an image
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_PLAIN
        strbgr = str(blue) + ',' + str(green)+','+str(red)
        cv2.putText(img,strbgr,(x,y),font,1,(0,255,255),1)
        cv2.imshow('image',img)

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('data/lena.jpg')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)     #this triggers a callback function whenever the mouse is clicked on
cv2.waitKey(0)
cv2.destroyAllWindows()