import cv2
cap = cv2.VideoCapture(0)
print("width:",cv2.CAP_PROP_FRAME_WIDTH)
print("hieght:",cv2.CAP_PROP_FRAME_HEIGHT)
cap.set(3,700)   # property id of CAP_PROP_FRAME_WIDTH(width of video) is 3
cap.set(4,720)      # # property id of CAP_PROP_FRAME_HIEGHT(hieght of video) is 4
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
