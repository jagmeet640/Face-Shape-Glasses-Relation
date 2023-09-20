# pip install opencv-python
import cv2
from cv2 import *

cam_port = 0
cam = cv2.VideoCapture(cam_port)

result, image = cam.read()

if result:
    cv2.imshow("Image", image)

    print(image)

    # cv2.waitKey(5000)

    cv2.waitKey(0)
    destroyWindow("Image")
else:
    print("No image")