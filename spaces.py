import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

plt.imshow(img)
plt.show()

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BRG to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# L*A*B to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_BGR2LAB)
cv.imshow('LAB to bgr', lab_bgr)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)