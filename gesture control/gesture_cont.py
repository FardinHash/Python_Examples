import cv2 as cv

# import numpy as np

img = cv.imread('resource/img/hand.jpg', 0)
flag, frame = cv.threshold(img, 70, 255, cv.THRESH_BINARY)

cont, _ = cv.findContours(frame.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

hull = [cv.convexHull(c) for c in cont]

final = cv.drawContours(img, hull, -1, (0, 0, 0))
cv.imshow('Original', img)
cv.imshow('thresh', frame)
cv.imshow('Final', final)

cv.waitKey(0)
cv.destroyAllWindows()
