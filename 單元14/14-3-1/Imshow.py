#!/usr/bin/env python
# -*- coding: utf8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture("http://127.0.0.1:8080/?action=stream?dummy=param.mjpg")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()






