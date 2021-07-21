# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 12:36:58 2021

@author: Abhimanyu
"""

import cv2
import os
import time
import HandTrackingModule as track

wcam, hcam = 640,480

currT = 0
prevT = 0
cap = cv2.VideoCapture(1)
cap.set(3, wcam)
cap.set(4, hcam)
det = track.handDetector()


def numFingers(landmarklist):
    tiplist =[8,12,16,20]
    status=[]
    if landmarklist[4][1]<landmarklist[5][1]:
        cv2.putText(img,"open", (landmarklist[4][1],landmarklist[4][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
        status.append(1)
    else:
        cv2.putText(img,"close", (landmarklist[4][1],landmarklist[4][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
        status.append(0)
    for i in tiplist:
        if lmslist[i][2]<lmslist[i-2][2]:
            cv2.putText(img,"open", (landmarklist[i][1],landmarklist[i][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(1)
        else:
            cv2.putText(img,"close", (landmarklist[i][1],landmarklist[i][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(0)
    return status
    
    
while True:
    _,img=cap.read()
    img=cv2.flip(img,1)
    img = det.findHands(img)
    lmslist = det.findPosition(img,draw = False)
    currT = time.time()
    fps = int(1/(currT-prevT))
    prevT = currT
            
    cv2.putText(img,"FPS:"+str(fps), (10,70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
    if len(lmslist)!=0:
        status=numFingers(lmslist)
        #print(status)
        totalFin = sum(status)
        cv2.putText(img,str(totalFin), (600,70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
    cv2.imshow("Frame", img)
    #cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break