import numpy as np
import cv2
import os, sys
from count import count


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc=cv2.cv.CV_FOURCC('X','V','I', 'D')
out = cv2.VideoWriter('sample_'+str(count)+'.avi',fourcc, 20.0, (640,480))
t = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

	t+=1	

        #frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & t == 20:
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
count+=1
os.remove('count.py')
f=open('count.py','w')
f.write('count='+str(count)+'')
f.close
