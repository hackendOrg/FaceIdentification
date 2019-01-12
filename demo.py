import cv2
from HackendUtils import face_recognition as fr

# new face classifier
faceClassifier = fr.get_face_detector()
# constructor gets the number on the camera connected to the computer
cam = cv2.VideoCapture(0)
BLUE = (255, 0, 0)

while True:
    # take a snapshot
    ret, image = cam.read()
    # detect face from image
    faces = fr.detect(faceClassifier, image)
    # print faces
    print(faces)
    # for every axis in face
    for (x, y, w, h) in faces:
        # draw a rectangle based on offset
        cv2.rectangle(image, (x, y),
                      (x + w, y + h), BLUE)
        cv2.imshow('Hackend\'s Face Recognition', image)
        cv2.waitKey(10)
