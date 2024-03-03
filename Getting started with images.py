import cv2
img= cv2.imread('data/lena.jpg',-1)
print(img)
cv2.imshow('image',img)  #Print the image pixel matrix
cv2.waitKey(5000)    #Method to hold the opened window until certain time
cv2.destroyAllWindows()   #Destroy all the windows created