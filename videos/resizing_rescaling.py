#resizing photo

import cv2 as cv
img = cv.imread('../photos/cat.jpg')
cv.imshow('cat',img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) 

resized_image = rescaleFrame(img)
cv.imshow('Resized Image',resized_image) 
cv.waitKey(0)




#resizing video

import cv2 as cv

capture = cv.VideoCapture('../photos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.75)
    cv.imshow('Video',frame)
    cv.imshow('video Resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



#this function only work for live video

"""def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)"""

