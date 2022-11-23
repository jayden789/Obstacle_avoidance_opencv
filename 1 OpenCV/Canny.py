import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()
    img = frame.copy()
    blur = cv2.bilateralFilter(img,9,40,40)
    edges = cv2.Canny(blur,50,100)
    cv2.imshow("Canny",edges)
    if cv2.waitKey(5) & 0xFF == ord("q"):

        break


cap.release()
cv2.destroyAllWindows()