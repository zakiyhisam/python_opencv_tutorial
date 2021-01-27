import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank img', blank)

cirle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)



masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked img', masked)

cv.waitKey(0)