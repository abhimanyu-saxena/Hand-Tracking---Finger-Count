# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:53:58 2021

@author: Abhimanyu
"""

import cv2
import time
import mediapipe as mp

class handDetector():
    def __init__(self, statMode = False, maxHands = 2, detConf = 0.5, trackConf = 0.5):
        self.statMode= statMode
        self.maxHands = maxHands
        self.detConf = detConf
        self.trackConf = trackConf
        
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.statMode , self.maxHands, 
                                        self.detConf, self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils
    
    def findHands(self, image, draw = True):
        RGBimg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(RGBimg)
        
        if self.results.multi_hand_landmarks:
            for eachHand in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, eachHand, self.mphands.HAND_CONNECTIONS)
        return image
    
    def findPosition(self, image, handNo= 0, draw = False):
        lmlist = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(hand.landmark):
                h,w,c = image.shape
                px , py = int(lm.x*w), int(lm.y*h)
                lmlist.append([id, px, py])
                
                if draw:
                    cv2.circle(image, (px,py), 10,(255,0,255), cv2.FILLED)
        return lmlist
    
def main():
    currT = 0
    prevT = 0
    cap = cv2.VideoCapture(1)
    det = handDetector()
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
               cv2.putText(img,"iTip", (lmslist[8][1],lmslist[8][2]), 
                           cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
           cv2.imshow("Frame", img)
           #cv2.waitKey(1)
           if cv2.waitKey(1) == ord('q'):
               cv2.destroyAllWindows()
               break
if __name__ == "__main__":
    main()
 
                