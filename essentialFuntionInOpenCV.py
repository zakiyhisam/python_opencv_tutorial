import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur image  *increase the kernelsize(5,5) to increase the blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#Edge Cascade (for less edges, use blurred img)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#dilating image (thicker line)
dilated = cv.dilate(canny, (7,7), iterations = 1)
cv.imshow('Dilated', dilated)

#eroding (thinner line)
eroded = cv.erode(dilated, (7,7), iterations= 1)
cv.imshow('Eroded', eroded)

#resize img
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)