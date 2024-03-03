import cv2
import numpy as np
#img = cv2.imread('data/lena.jpg',-1)
img = np.zeros([512,512,3],np.uint8)  #Image generation by numpy library
img = cv2.line(img,(0,0),(255,255),(0,0,255),10)
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,255),10)
img = cv2.rectangle(img,(245,10),(25,245),(0,0,255),-1)
img = cv2.circle(img,(0,0),200,(245,65,74),10)
font = cv2.FONT_HERSHEY_COMPLEX  #selecting font
img = cv2.putText(img,'OpenCV',(10,500),font,3,(255,0,0),10,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#common arguement list ---> (img_name,start point,endpoint,colour,thickness)