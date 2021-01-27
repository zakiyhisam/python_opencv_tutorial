import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

#splitting img
b,g,r= cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

blue=cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('merged blue', blue)
cv.imshow('merged green', green)
cv.imshow('merged red', red)

#merge img
merged = cv.merge([b,g,r])
cv.imshow('merged image', merged)

cv.waitKey(0)