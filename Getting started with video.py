import cv2
#cap = cv2.VideoCapture('data/tree.avi')  for importing images from the local machine
cap = cv2.VideoCapture(0)  #For reading the image
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) #arguements: 1.Name of file  2. fourcc code   3.no.of frames/sec   4.size of video
print("Is the video is opened:",cap.isOpened())
framenum = 0
while(True):
    ret, frame = cap.read()  #Checking if each pixels in the video exists or not
    framenum+=1
    if ret == True:
        print("Frame=",framenum)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Converting image to gray
        print("width =",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print("hieght =",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1)== ord('q'):
            break
    else:
        break
cap.release()  #Release all the captured resources
out.release()
cv2.destroyAllWindows()
