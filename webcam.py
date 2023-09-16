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

# Flag to indicate whether the user wants to quit
quit_requested = False

# Start a loop to capture frames from the webcam
while not quit_requested:
    # Capture the frame
    ret, frame = cap.read()

    # If the frame was not captured, break the loop
    if not ret:
        break

    # Display the frame
    cv2.imshow("Webcam", frame)

    # Check for user input
    key = cv2.waitKey(1)

    # If the key is 'q', set the quit flag to True
    if key == ord('q'):
        quit_requested = True

# Release the webcam
cap.release()

# Close the window
cv2.destroyAllWindows()
