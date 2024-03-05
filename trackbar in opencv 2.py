import cv2
import numpy as np
#img = cv2.imread('data/lena.jpg') 
cv2.namedWindow('image')
def nothing(x):
    print(x)
cv2.createTrackbar('cp','image',10,400,nothing)  # creation of trackbar arguments: name of trackbar, name of window, intial value, final value, callback function

switch = 'color/gray'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    img = cv2.imread('data/lena.jpg')
    pos = cv2.getTrackbarPos('cp','image')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,str(pos),(50,150),font,4,(0,0,255))
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

    swi = cv2.getTrackbarPos(switch,'image')
    if swi == 0:
        pass
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',img)
cv2.destroyAllWindows()