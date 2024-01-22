import cv2

# Function to capture a picture
def capture_picture(image):
    cv2.imshow("Captured Picture", image)
    cv2.waitKey(0)
    cv2.destroyWindow("Captured Picture")

# Working with the camera
cam_port = 0
cam = cv2.VideoCapture(cam_port)

while True:
    # Read a frame from the camera
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Display the current frame
    cv2.imshow("Video", frame)

    # Check for key events
    key = cv2.waitKey(1)

    # Press spacebar to capture a picture
    if key == 32:  # ASCII code for spacebar
        capture_picture(frame)

    # Press Esc to exit the program
    elif key == 27:
        break

# Release the camera and close the window
cam.release()
cv2.destroyAllWindows()
