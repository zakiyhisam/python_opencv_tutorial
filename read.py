import cv2 as cv

#resize frame of video on specific scale 1=width 0=height of frame, works for all types
def rescaleFrame(frame, scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

#change resolution, only works for live video etc webcam or camera
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread('Resources/Photos/cat.jpg') #read image source

cv.imshow('Cat', img) #show image in new window (name window, image to show)

resized_image = rescaleFrame(img) #resize image
cv.imshow('Image_resize', resized_image) 
cv.waitKey(0) #specific delay in milisecond to close window

img_large = cv.imread('Resources/Photos/cat_large.jpg')


while True:
    isTrue, frame = capture.read() #read video frame by frame
    frame_resized = rescaleFrame(frame) #using rescaleFrame def
    cv.imshow('Video', frame)   #view video
    cv.imshow('Video Resized',frame_resized)    #view resized video
    if cv.waitKey(20) & 0xFF==ord('d'): #wait key d to break or break until no more frame read in while loop
        break
#remember, if error something that would mean the capture read frame have finished read frame of the video.
capture.release()
cv.destroyAllWindows() 

