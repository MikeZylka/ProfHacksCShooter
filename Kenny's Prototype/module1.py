import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
face_cascade.load('C:\\Users\\kenny\\source\\repos\\Face Tracking\\haarcascade_frontalface_alt.xml')
j = 0 

font = cv2.FONT_HERSHEY_PLAIN

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    channing = cv2.imread('C:\\Users\\kenny\\source\\repos\\Face Tracking\channing.png')
    bord = cv2.BORDER_CONSTANT
    for (x, y, w, h) in faces:
        newChanning = cv2.resize(channing, (w,h))
        heightTop = img.shape[0] - (y - newChanning.shape[0])
        heightBottom = img.shape[0] - ( y - (newChanning.shape[0] - w))
        widthLeft = img.shape[1] - (x - newChanning.shape[1])
        widthRight = img.shape[1] - (x - (newChanning.shape[1] - w))
        print(f"{heightTop}, {heightBottom}, {widthLeft}, {widthRight}")
        newChanning = cv2.copyMakeBorder(newChanning, heightTop, heightBottom, widthLeft, widthRight, bord)
        img = cv2.addWeighted(newChanning, .5, img, .5, 0)
        #img = channing_roi
        print(f"Person detected at {x}, {y}, {w}, {h}")
    cv2.imshow('Video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows
