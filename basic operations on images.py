import cv2
img = cv2.imread('data/messi5.jpg')
img2 = cv2.imread('data/opencv-logo.png')
print(img.shape) #returns the tuple of number of rows and columns
print(img.size)  #returns the total number of pixels accessed
print(img.dtype)  #returns the data type of the image
b,g,r=cv2.split(img)  #Splits the channels into b,g,r
img = cv2.merge((b,g,r))

#ball = img[280:340,330:390]
#img[273:333, 100:160] = ball
img2=cv2.resize(img2,(512,512))
img=cv2.resize(img,(512,512))
#dest = cv2.add(img,img2)
dest = cv2.addWeighted(img,0.6,img2,0.4,0)
cv2.imshow('image',dest)
cv2.waitKey(0)
cv2.destroyAllWindows()