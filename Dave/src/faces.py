import numpy as np
import cv2
from datetime import *

face_cascade = cv2.CascadeClassifier('C:/Users/mikez/Documents/Git/Hackathons/ProfHacks/Dave/src/cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(1)
sTime = datetime.now().second
dAve = []
width = int(cap.get(3))
height = int(cap.get(4))

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors = 5)
    cTime = datetime.now().second
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        dAve = dAve + [(8.5 * 575.0034602076125)/ w]
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y-60:y+h+60, x-20:x+w+20]

        color = (255, 0, 0)
        thickness = 4
        x1 = x + w
        y1 = y + h
        cv2.rectangle(img, (width//2, 0), (width//2, height), (0,0,255), 2)
        cv2.rectangle(img, (0,height//2), (width, height//2), (0,0,255), 2)
        cv2.rectangle(img, (x,y), (x1, y1), color, thickness)

        com = (x+(w//3) + (((x+w-(w//3)) - (x+(w//3))) // 2), y+h-(h//3) + ((y+h+(h//7)) - (y+h-(h//3)))//2 ) 

        
        dy = (height // 2) - com[1]
        #print(dy) 

        dx = com[0] - (width // 2) 
        #print(dx)

        PTI = (8.5 * dy) / h
        print(PTI)

        if (sTime != cTime):
            sum = 0
            for i in dAve:
                sum = sum + i
            D = sum / len(dAve)
            #print(D)
            dAve = []
            sTime = datetime.now().second
            cTime = datetime.now().second

        cv2.putText(img, f"Distance: {D}", (x+(w//3), y+h-(h//3)), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
        

        cv2.rectangle(img, (x+(w//3), y+h-(h//3)), (x+w-(w//3), y+h+(h//7)), (0,255,0), 2)

        cv2.rectangle(img, com, com, (0,255, 255), 5)
        
        #img_item = "data.png"
        #cv2.imwrite(img_item, roi_color)

        #cv2.rectangle(img, (x+(w//5), y+(h//2 + h//5)), (x+w-(w//5), y+h-(h//10)), (0,255,0), 2)

    cv2.imshow('Tracking', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows()

