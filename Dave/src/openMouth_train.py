import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images/open-mouth")

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png"):
            path = os.path.join(root, file)
            print(path)