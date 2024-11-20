import cv2
import sys
import numpy as np


#source = sys.argv[1]
#img = cv2.imread(source)
#cv2.imshow("frame_1", img)

min = np.array([110, 50, 50])
max = np.array([130, 255, 255])

cam = cv2.VideoCapture(1)

while True:
  ret, frame = cam.read()
  hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv_img, min, max)

  if not ret:
    break

  cv2.imshow("camera", frame)
  cv2.imshow("mask", mask)
  result = cv2.bitwise_and(frame, frame, mask=mask) 
  cv2.imshow("result", result)

  if cv2.waitKey(1) == ord('q'):
    break

cam.release()
cv2.destroyAllWindows()

