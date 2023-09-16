from roboflow import Roboflow
rf = Roboflow(api_key="eurWhLwiwz1glktp3OqT")
project = rf.workspace("roboflow-58fyf").project("rock-paper-scissors-sxsw")
dataset = project.version(12).download("yolov7")

import cv2 


# Get the webcam
cap = cv2.VideoCapture(0)


# Check if the webcam is opened
if not cap.isOpened():
  print("Error opening webcam")
  exit()

# Get the frame size
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create a window to display the webcam feed
cv2.namedWindow("Webcam")

# Start a loop to capture frames from the webcam
while True:
  # Capture the frame
  ret, frame = cap.read()

  # If the frame was not captured, break the loop
  if not ret:
    break

  # Display the frame
  cv2.imshow("Webcam", frame)

  # Wait for a key press
  key = cv2.waitKey(1)

  # If the key is `q`, break the loop
  user_input = input("press q to quit")
  if user_input == 'q':
    break

# Release the webcam
cap.release()

# Close the window
cv2.destroyAllWindows()