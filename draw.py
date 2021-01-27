import cv2 as cv
import numpy as np

#create a dummy blank image (width, height, no of colour channel)
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)


img = cv.imread('Resources/Photos/cat.jpg')
#cv.imshow('Cat', img)

#paint image a certain colour [starting pixel,end pixel]
#blank[:] = 0,0,255
#cv.imshow('Red', blank)
#blank[300:400,500:600] = 0,255,0
#cv.imshow('Partial colour', blank)

#draw rectangle (-1 to fill colour rectangle on thickness)
cv.rectangle(blank,(0,0),(250,500),(255,0,0), thickness=1)
cv.imshow('Rectangle', blank)

#draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness= 3)
cv.imshow('Circle', blank)

#draw a line
cv.line(blank,(0,blank.shape[0]//2,), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness= 3)
cv.imshow('line',blank)

#write a text (1.0=scale, 2=font thickness)
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0) 