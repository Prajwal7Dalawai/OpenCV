import cv2
img= cv2.imread('data/lena.jpg',-1)
print(img)
cv2.imshow('image',img)  #Print the image pixel matrix
k = cv2.waitKey(0)    #Method to hold the opened window until certain time(in ms)

if k==27 and 0xFF:
   cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('image_lena.png',img)  #Writing the image, also this method is used to save the image in local machine
    cv2.destroyAllWindows()   #Destroy all the windows created
