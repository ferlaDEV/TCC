import numpy as np
import cv2
import os

BLUE_COLOR = (255, 0, 0)
STROKE = 2

clf = cv2.CascadeClassifier('/home/ferla/Documentos/Reconhecimento/haarcascade_frontalface_alt2.xml')
clf2 = cv2.CascadeClassifier('/home/ferla/Documentos/Reconhecimento/haarcascade_eye.xml')
clf3 = cv2.CascadeClassifier('/home/ferla/Documentos/Reconhecimento/haarcascade_smile.xml')
cap = cv2.VideoCapture(0)

while(not cv2.waitKey(20) & 0xFF == ord('q')):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(gray)
        eyes = clf2.detectMultiScale(gray)
        smile = clf3.detectMultiScale(gray)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), BLUE_COLOR, STROKE)
        for x, y, w, h in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), RED_COLOR, STROKE)
        for x, y, w, h in smile:
            cv2.rectangle(frame, (x, y), (x+w, y+h), YELLOW_COLOR, STROKE)
        cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()
