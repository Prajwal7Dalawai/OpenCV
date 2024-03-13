'''#
First, a classifier (namely a cascade of boosted classifiersmworking with haar-like features) is trained with a few hundred sample views
of a particular object (i.e., a face or a car), called positive examples, that are scaled to the same size (say, 20x20), and
negative examples - arbitrary images of the same size.
#'''
import cv2
img = cv2.imread('data/test.png')


cv2.waitKey(0)
cv2.destroyAllWindows()