import cv2
import numpy as np

def process(img):
    print(img.shape)
    h = img.shape[0]
    w = img.shape[1]
    region_of_interest_vertices = [
    (0,h),
    (w,h),
    (180,h/2.5)
    ]

    def region_of_interest(img,vertices):
        mask = np.zeros_like(img)
        #channel_count = img.shape[2]
        match_color = 255
        cv2.fillPoly(mask,vertices,match_color)
        masked_image = cv2.bitwise_and(img,mask)
        return masked_image

    def drawline(img,lines):
        img = np.copy(img)
        blank_image = np.zeros((img.shape[0],img.shape[1],3), dtype = np.uint8)
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),thickness=1)
        img = cv2.addWeighted(img,0.8,blank_image,1,0.0)
        return img
    #cropped_image = region_of_interest(img,np.array([region_of_interest_vertices],np.int32))
    gray_image = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image,100,200)
    cropped_image = region_of_interest(canny_image,np.array([region_of_interest_vertices],np.int32))
    lines = cv2.HoughLinesP(cropped_image,rho=6,theta=np.pi/60,threshold=120,lines=np.array([]),minLineLength=40,maxLineGap=25)
    image_with_lines = drawline(img,lines)
    return image_with_lines

cap = cv2.VideoCapture('vtest.avi')
while(cap.isOpened()):
    ret,frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()