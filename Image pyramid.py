#Pyramid or pyramid representation is a type multi-scale signal representation in which a signal or an image is subject to repeated 
#smoothing  and subsampling
#Two types of Pyramid: 1.Gausian Pyramid  2. Laplacian Pyramid
import cv2
import numpy as np
img = cv2.imread('data/lena.jpg',-1)
#1.Gausian Pyramid
'''#lr = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr)
hr = cv2.pyrUp(img)
cv2.imshow('image',img)
cv2.imshow('paidimage',lr)
cv2.imshow('pimage',hr)#'''

layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

#Laplacian Pyramid are formed from gausian pyramid
    #A level of Laplacian pyramid is formed by a difference between that level in Gausian Pyramid and expanded vesrion of its upper
    #level in Gausian Pyramid
lp = [layer]
for i in range(5,0,-1):
    gausian_ext = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gausian_ext)
    cv2.imshow(str(i),laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()