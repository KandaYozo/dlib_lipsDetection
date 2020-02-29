from extract_lips import *



filename = "close.png"
frame, mouth_roi = extractLips(filename)
print(mouth_roi)
cv2.imshow("frame image", frame)
cv2.waitKey(0)

