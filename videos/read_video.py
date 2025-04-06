import cv2 as cv

capture = cv.VideoCapture('../photos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()