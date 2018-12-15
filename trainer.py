import cv2
import os
import numpy as np
from PIL import Image
from name_to_id import DataHandler

# create recognizer entity
recognizer = cv2.face.LBPHFaceRecognizer_create()
# path
cascadePath = "Classifiers/face.xml"
# Create classifier entity
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'data_set'
# load map
data_handler = DataHandler()


def get_images_and_labels(path):
    # paths getter
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    # runs for every image
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image from json map
        label = data_handler.get_id_by_name(str(os.path.split(image_path)[1].split(".")[0]))
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(label)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(10)
    # return the images list and labels list
    return images, labels


# runs function
images, labels = get_images_and_labels(path)

# train
if not os.path.exists("trainer"):
    os.mkdir("trainer")
# training
recognizer.train(images, np.array(labels))
# save model
recognizer.save('trainer/trainer.yml')
cv2.destroyAllWindows()
