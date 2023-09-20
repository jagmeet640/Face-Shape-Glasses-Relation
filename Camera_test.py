# pip install opencv-python
import cv2
from cv2 import *

cam_port = 0
cam = cv2.VideoCapture(cam_port)

result, image = cam.read()

if result:
    cv2.imshow("Image", image)

    waitkey(0)
    destroyWindow("Image")
else:
    print("No image")