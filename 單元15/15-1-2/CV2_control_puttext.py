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

    if lastCmd == ord('w'):
        cv2.putText(frame,'W',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),3,cv2.LINE_AA)
    else:
        cv2.putText(frame,'W',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3,cv2.LINE_AA)

    if lastCmd == ord('s'):
        cv2.putText(frame,'S',(50,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),3,cv2.LINE_AA)
    else:
        cv2.putText(frame,'S',(50,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3,cv2.LINE_AA)

    if lastCmd == ord('a'):
        cv2.putText(frame,'A',(30,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),3,cv2.LINE_AA)
    else:
        cv2.putText(frame,'A',(30,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3,cv2.LINE_AA)

    if lastCmd == ord('d'):
        cv2.putText(frame,'D',(70,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),3,cv2.LINE_AA)
    else:
        cv2.putText(frame,'D',(70,80),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3,cv2.LINE_AA)
        
    if lastCmd == ord('x'):
        cv2.putText(frame,'X',(50,110),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),3,cv2.LINE_AA)
    else:
        cv2.putText(frame,'X',(50,110),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),3,cv2.LINE_AA)

    cv2.imshow('frame',frame)
