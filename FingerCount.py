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
while True:
    _,img=cap.read()
    img=cv2.flip(img,1)
    img = det.findHands(img)
    lmslist = det.findPosition(img,draw = False)
    currT = time.time()
    fps = int(1/(currT-prevT))
    prevT = currT
            
    cv2.putText(img,str(fps), (10,70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
    if len(lmslist)!=0:
        status=[]
        
        #thumb
        if lmslist[4][1]<lmslist[5][1]:
            cv2.putText(img,"open", (lmslist[4][1],lmslist[4][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(1)
        else:
            cv2.putText(img,"close", (lmslist[4][1],lmslist[4][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(0)
        #index finger
        if lmslist[8][2]<lmslist[6][2]:
            cv2.putText(img,"open", (lmslist[8][1],lmslist[8][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(1)
        else:
            cv2.putText(img,"close", (lmslist[8][1],lmslist[8][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(0)
        #middle finger
        if lmslist[12][2]<lmslist[10][2]:
            cv2.putText(img,"open", (lmslist[12][1],lmslist[12][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(1)
        else:
            cv2.putText(img,"close", (lmslist[12][1],lmslist[12][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(0)
        #ring finger
        if lmslist[16][2]<lmslist[14][2]:
            cv2.putText(img,"open", (lmslist[16][1],lmslist[16][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(1)
        else:
            cv2.putText(img,"close", (lmslist[16][1],lmslist[16][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(0)
        #little finger
        if lmslist[20][2]<lmslist[18][2]:
            cv2.putText(img,"open", (lmslist[20][1],lmslist[20][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(1)
        else:
            cv2.putText(img,"close", (lmslist[20][1],lmslist[20][2]), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            status.append(0)
        
#        cv2.putText(img,"iTip", (lmslist[8][1],lmslist[8][2]), 
#        cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
        print(status)
    cv2.imshow("Frame", img)
    #cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break