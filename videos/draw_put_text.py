import cv2 as cv

import numpy as np

#it create a blank image where we are going to draw or put text

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

# 1. Paint the image a certain colour

"""green color"""

blank[:] = 0,255,0
cv.imshow('Green',blank)

"""Red color"""

blank[:] = 0,0,255
cv.imshow('Red',blank)

cv.waitKey(0)
