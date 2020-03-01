import os
import cv2
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images/open-mouth")


face_cascade = cv2.CascadeClassifier('C:/Users/mikez/Documents/Git/Hackathons/ProfHacks/Dave/src/cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFa


current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png"):
            path = os.path.join(root, file)
            print(path)
            label = "open-mouth"
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
                
            id_ = label_ids[label]
            print(label_ids)

            pil_image = Image.open(path).convert("L")
            image_array = np.array(pil_image, "uint8")
            print(image_array)
            #faces = face_cascade.detectMultiScale(image_array)

            x_train.append(image_array)
            y_labels.append(id_)

#print(y_labels)
#print(x_train)

with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)


recognizer.save("trainner.yml")
