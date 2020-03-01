import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/mikez/Documents/Git/Hackathons/ProfHacks/Dave/src/cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(1)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors = 5)

    for (x,y,w,h) in faces:
        print(x,y,w,h)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y-60:y+h+60, x-20:x+w+20]

        color = (255, 0, 0)
        thickness = 4
        x1 = x + w
        y1 = y + h
        cv2.rectangle(img, (x,y), (x1, y1), color, thickness)
        
        #img_item = "data.png"
        #cv2.imwrite(img_item, roi_color)

        #cv2.rectangle(img, (x+(w//5), y+(h//2 + h//5)), (x+w-(w//5), y+h-(h//10)), (0,255,0), 2)

    cv2.imshow('Tracking', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows()

