import cv2
import time
from botControl import run_ActionGroup

def forward():
   run_ActionGroup('1',1)

def stop():
    run_ActionGroup('0',1)

def backward():
    run_ActionGroup('2',1)  

def right():
    run_ActionGroup('4',1)

def left():
    run_ActionGroup('3',1)

cap = cv2.VideoCapture("http://127.0.0.1:8080/?action=stream?dummy=param.mjpg")


lastCmd = ''

while 1:
    key = ''
    ret,frame = cap.read()
    commandList= {ord('w'):forward,
                  ord('s'):stop,
                  ord('a'):left,
                  ord('x'):backward,
                  ord('d'):right}
    key = cv2.waitKey(1) & 0xff
    
    if key == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break
    elif key in commandList:
        lastCmd = key
        commandList[key]()
        print(key)
    else:
        pass
    
    cv2.imshow('frame',frame)
