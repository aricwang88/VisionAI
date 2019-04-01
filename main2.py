import socket
import sys
import os
import numpy as np
import pdb

import cv2
import time

from Image import *
from Utils import *

font = cv2.FONT_HERSHEY_SIMPLEX
direction = 0
Images=[]
N_SLICES = 4

for q in range(N_SLICES):
    Images.append(Image())

def nothing(x):
    pass

if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    
    cap.set(3, 640)
    cap.set(4, 480)

    while(cap.isOpened()):
        ret, frame = cap.read()

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        direction = 0
        img = RemoveBackground(frame, False)
        if img is not None:
            t1 = time.clock()
            SlicePart(img, Images, N_SLICES)
            for i in range(N_SLICES):
                direction += Images[i].dir

            fm = RepackImages(Images)
            t2 = time.clock()
            cv2.putText(fm,"Time: " + str((t2-t1)*1000) + " ms",(10, 470), font, 0.5,(0,0,255),1,cv2.LINE_AA)
            cv2.imshow("Selfdriving Car", fm)
            #Send dir to car.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break 
        #cv2.imshow('frame',frame)
        else:
            break	

    cap.release()
    cv2.destroyAllWindows()

