import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/mikez/Documents/Git/Hackathons/ProfHacks/Dave/src/cascades/data/haarcascade_frontalface_alt.xml')
#nose_cascade = cv2.CascadeClassifier('C:/Users/mikez/Documents/Git/Hackathons/ProfHacks/Dave/src/cascades/third-party/Nose18x15.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors = 5)

    for (x,y,w,h) in faces:
        print(x,y,w,h)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        color = (255, 0, 0)
        thickness = 4
        x1 = x + w
        y1 = y + h
        cv2.rectangle(img, (x,y), (x1, y1), color, thickness)

        #nose = nose_cascade.detectMultiScale(roi_gray)
        #for (mx, my, mw, mh) in mouth:
            #cv2.rectangle(roi_color, (mx,my), (mx+mw, my+mh), (0,255,0), 2)


    cv2.imshow('Tracking', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows()

