#!/usr/bin/env python
# -*- coding: utf8 -*-

import datetime
import time
import numpy as np
import cv2
times = 0;
if __name__ == '__main__':
    #影像入侵偵測程式碼
    
    cap = cv2.VideoCapture("http://127.0.0.1:8080/?action=stream?dummy=param.mjpg")
    cap.set(3,640)  #寬
    cap.set(4,480)  #高
    k=1
    lasttime = cv2.getTickCount()
    while(True):
    # Capture frame-by-frame
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        small = cv2.resize(frame,(64, 48), interpolation = cv2.INTER_AREA)
        if (k == 1):
            smallpre = small.copy()
            k = 0
        diff = cv2.subtract(smallpre,small)
        diffmean = diff.mean()
        nowtime = cv2.getTickCount()
        #print( diffmean)
        t = (nowtime - lasttime)/cv2.getTickFrequency()
        if ((diffmean > 5) and (t > 1)) :
            times = times + 1
            cv2.imwrite("alert.jpg", frame)
            #time.sleep(1)
            print( "------------detector--------------")
            print( times)
            lasttime = cv2.getTickCount()
        smallpre = small.copy()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
