# library
import cv2 as cv

face_cascade = cv.CascadeClassifier('resource/haarcascade_frontalface_default.xml')
face_cascade_eye = cv.CascadeClassifier('resource/haarcascade_eye.xml')

cap = cv.VideoCapture(0)
while cap.isOpened():

    flag, img = cap.read()

    gray = cv.cvtColor(
        img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        img, 1.1, 7)
    eyes = face_cascade_eye.detectMultiScale(img, 1.1, 7)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

    for (a, b, c, d) in eyes:
        cv.rectangle(img, (a, b), (a + c, b + d), (255, 0, 0), 1)

    cv.imshow("img", img)
    c = cv.waitKey(1)
    if c == ord("q"):
        break

cv.release()
cv.destroyAllWindows()
