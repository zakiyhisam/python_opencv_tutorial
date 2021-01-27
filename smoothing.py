import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cats', img)

#averaging (increase kernel size to increase blur image)
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian blur', gauss)

#median blur
median = cv.medianBlur(img, 7)
cv.imshow('median blur', median)

#bilateral blur
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)