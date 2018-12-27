import cv2
import os
from HackendUtils import face_recognition as fr

#מצלמה ראשית
camera = cv2.VideoCapture(0)

#מחזיר ערכים לזיהוי
detector = fr.get_face_detector()

#קורא תמונה מהמצלמה
status, image = camera.read()

#להפוך את התמונה לאפור
gray_matrix = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# לחכות  0.1 שניות
cv2.waitKey(10)


#מחזיר ערכים של הפנים מהתמונה
faces = detector.detectMultiScale(gray_matrix, scaleFactor=1.2,
                                      minNeighbors=5, minSize=(100, 100),
                                      flags=cv2.CASCADE_SCALE_IMAGE)

#שומר את התמונה
cv2.imwrite(curr_file_name,
            gray_matrix[y_axis - PIXELS_OFFSET:y_axis + h_axis +
                                               PIXELS_OFFSET,
            x_axis - PIXELS_OFFSET:x_axis + w_axis + PIXELS_OFFSET])

#משחרר את המצלמה
# close
camera.release()
# exit window
cv2.destroyAllWindows()
# printing to the json file
data_handler.to_json()





















