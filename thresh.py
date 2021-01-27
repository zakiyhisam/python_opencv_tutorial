import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

#inverse simple thresholding
threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

#Adaptive Thresholding (for inv just add _INV on cv.THRESH_BINARY)
adaptive_thresh= cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)