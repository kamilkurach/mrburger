import cv2
import sys
import numpy as np


#source = sys.argv[1]
#img = cv2.imread(source)
#cv2.imshow("frame_1", img)

min = np.array([110, 50, 50])
max = np.array([130, 255, 255])

#cam = cv2.VideoCapture(1)
cam = cv2.VideoCapture('test_drive_3.h264')

while True:
  ret, frame = cam.read()
  hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  mask = cv2.inRange(hsv_img, min, max)
   
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.6)
      
  edges = cv2.Canny(blurred, 80, 130)

  if not ret:
    break

  cv2.imshow("camera", frame)
  cv2.imshow("edges", edges)
  cv2.imshow("mask", mask)
  result = cv2.bitwise_and(frame, frame, mask=mask) 
  cv2.imshow("result", result)
  white_pix = np.sum(result == 255) 
  black_pix = np.sum(result == 0) 
  
  print(white_pix, black_pix)
  if cv2.waitKey(1) == ord('q'):
    break

cam.release()
cv2.destroyAllWindows()

