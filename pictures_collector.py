import cv2
import os
# Create camera entity
camera = cv2.VideoCapture(0)

# Create a detector entity
detector = cv2.CascadeClassifier('Classifiers/face.xml')
PICTURES_NUMBER = 20
index = 0
PIXELS_OFFSET = 50
name=raw_input('enter your first name')
if not os.path.exists("data_set"):
    os.mkdir("data_set")
while index < PICTURES_NUMBER:
    # gets the next snap shot
    status, image = camera.read()
    # for image processing to be accurate, the image quality should be in the gray scale rgb
    gray_matrix = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gets a map of arrays of mathematical values of different vectors of the picture
    faces = detector.detectMultiScale(gray_matrix, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
    # runs for every axis
    for (x, y, w, h) in faces:
        index += 1
        # writes the image , jpg < png
        cv2.imwrite("data_set/" + name + '.' + str(index) + ".jpg",
                    gray_matrix[y - PIXELS_OFFSET:y + h + PIXELS_OFFSET, x - PIXELS_OFFSET:x + w + PIXELS_OFFSET])
# close
camera.release()
# exit window
cv2.destroyAllWindows()

