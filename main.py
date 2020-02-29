import cv2
import numpy as np
from FR import *
from lip_detection import *



img = readFrame()

detector,predictor = initlizeDlib()

resized = resizeImage(img)
cv2.imshow("initial image", resized)
cv2.waitKey(0)

frame = lipDetection(resized, detector, predictor)
cv2.imshow("frame image", frame)
cv2.waitKey(0)
