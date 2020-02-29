import cv2
import numpy as np
import dlib


def lipDetection(frame,detector,predictor):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        for n in range(0,68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame,(x,y),3,(255,0,0),1)
    return frame