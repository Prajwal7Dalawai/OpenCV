import cv2
import pytesseract as py

def ocr_core(img):
    text = py.image_to_string(img)
    return text

img = cv2.imread('data/imageTextN.png')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img= cv2.medianBlur(img,5)
img = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
print(ocr_core(img))