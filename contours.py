import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/test.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

#convert img to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#canny image
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny) 

#threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

#define contour
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

#draw the contour from blank img
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)