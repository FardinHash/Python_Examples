import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)  

# Create a background subtractor
bg_subtractor = cv.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(frame)

    # Thresholding
    _, thresh = cv.threshold(fg_mask, 70, 255, cv.THRESH_BINARY)

    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        hand_contour = max(contours, key=cv.contourArea)

        hull = cv.convexHull(hand_contour)

        cv.drawContours(frame, [hand_contour], 0, (0, 255, 0), 2)
        cv.drawContours(frame, [hull], 0, (0, 0, 255), 3)

        M = cv.moments(hand_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv.circle(frame, (cx, cy), 5, (255, 255, 255), -1)

    cv.imshow('Hand Gesture Control', frame)

    # Press 'q' to exit
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
