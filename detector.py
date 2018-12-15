import cv2
from name_to_id import DataHandler

# create image recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
# load the training data
recognizer.read('trainer/trainer.yml')
# classifier path
classifierPath = "Classifiers/face.xml"
# new face classifier
faceClassifier = cv2.CascadeClassifier(classifierPath)
# load data
data_handler = DataHandler()
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX  # Creates a font
OFFSET = 50

while True:
    # take a snapshot
    ret, image = cam.read()
    # convert to gray matrix
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect face from image
    faces = faceClassifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),
                                            flags=cv2.CASCADE_SCALE_IMAGE)
    # for every axis in face
    for (x, y, w, h) in faces:
        # make a prediction base on trainer data
        predicted, conf = recognizer.predict(gray[y:y + h, x:x + w])
        # draw a rectangle based on offset
        cv2.rectangle(image, (x - OFFSET, y - OFFSET), (x + w + OFFSET, y + h + OFFSET), (225, 0, 0), 2)
        # convert prediction id to a name based on json
        predicted = data_handler.get_name_by_id(predicted)
        # put text on image
        cv2.putText(image, str(predicted) + "--" + str(conf), (x, y + h), font, 1,
                    (0, 0, 255), 2)  # Draw the text
        # show the image
        cv2.imshow('im', image)
        cv2.waitKey(10)
