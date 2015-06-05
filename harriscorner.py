import cv2
import numpy as np

filename = 'image03.png'
img = cv2.imread(filename)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.equalizeHist(img)

gray = np.float32(img)
dst = cv2.cornerHarris(img,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
