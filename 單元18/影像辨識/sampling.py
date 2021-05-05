import numpy as np
import cv2
import time
import numpy
import serial

WIDTH = 640
HEIGHT = 480
SPEED = 25
BINARY_THRESHOLD = 120

cap = cv2.VideoCapture("http://127.0.0.1:8080/?action=stream?dummy=param.mjpg")
cap.set(3,WIDTH)
cap.set(4,HEIGHT)
fourcc = cv2.VideoWriter_fourcc(*'XVID')#編碼格式
video = cv2.VideoWriter('video.avi', fourcc, 9.5, (WIDTH, HEIGHT))

while 1:
    ret,img = cap.read()
    video.write(img)
    cv2.rectangle(img,(120,40), (520,440),(0, 255, 0))
    cv2.imshow('recording',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
