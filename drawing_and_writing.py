import numpy as np
import cv2

img = cv2.imread('banana_leclerc.jpg',cv2.IMREAD_COLOR)
cv2.circle(img,(150,63), 55, (0,0,255), 4)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'banana leclerc',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
