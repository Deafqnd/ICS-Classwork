import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while(1): 
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([124,20,27])
    upper_green = np.array([126,97,98])

    dark_red = np.uint8([[[12,22,121]]])
    dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
