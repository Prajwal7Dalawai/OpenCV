'''#
First, a classifier (namely a cascade of boosted classifiersmworking with haar-like features) is trained with a few hundred sample views
of a particular object (i.e., a face or a car), called positive examples, that are scaled to the same size (say, 20x20), and
negative examples - arbitrary images of the same size.
#'''
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()