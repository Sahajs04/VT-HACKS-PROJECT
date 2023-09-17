from roboflow import Roboflow
import cv2
count = 0
rf = Roboflow(api_key="sKsQzha8jrnm9Onvmp6p")
project = rf.workspace().project("rock-paper-scissors-sxsw")
model = project.version(11).model

# Get the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened
if not cap.isOpened():
    print("Error opening webcam")
    exit()

# Get the frame size
frame_width = int(cap.get(3))
# Create a window to display the webcam feed
cv2.namedWindow("Webcam")

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
  # f.read() methods returns a tuple, first element is a bool 
  # and the second is frame
    ret, frame = cap.read()
    if ret == True:
        # save frame as a “temporary” jpeg file
        cv2.imwrite('temp.jpg', frame)
        # run inference on “temporary” jpeg file (the frame)
        predictions = model.predict('temp.jpg')
        predictions_json = predictions.json()
        # printing all detection results from the image
        print(predictions_json)

        # accessing individual predicted boxes on each image
        for bounding_box in predictions:
            # x0 = bounding_box['x'] - bounding_box['width'] / 2#start_column
            # x1 = bounding_box['x'] + bounding_box['width'] / 2#end_column
            # y0 = bounding_box['y'] - bounding_box['height'] / 2#start row
            # y1 = bounding_box['y'] + bounding_box['height'] / 2#end_row
            class_name = bounding_box['class']
            confidence_score = bounding_box['confidence']
        
            detection_results = bounding_box
            class_and_confidence = (class_name, confidence_score)
            print(class_and_confidence, '\n')

    if cv2.waitKey(10) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()