import cv2
import sys
import time
import io
import serial

print('系統啟動中......')

KERAS_MODEL_WEIG = 'dnn_model.h5'
KERAS_MODEL_NAME = 'dnn_model.model'
model = ''

def dnnInit():
    global model
    
    from keras.models import Sequential
    from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D

    model = Sequential()
    # Create CN layer 1
    model.add(Conv2D(filters=32, 
                     kernel_size=(3,3),  
                     padding='same',  
                     input_shape=(160,160,3), 
                     activation='relu'))

    model.add(Conv2D(filters=48,
                     kernel_size=(1,1),
                     padding='same',
                     input_shape=(160,160,3),
                     activation='relu'))
    # Create Max-Pool 1
    model.add(MaxPooling2D(pool_size=(2,2)))

    # Create CN layer 2
    model.add(Conv2D(filters=24,
                     kernel_size=(3,3),
                     padding='same',
                     input_shape=(160,160,3),
                     activation='relu'))

    # Create CN layer 3
    model.add(Conv2D(filters=24,
                     kernel_size=(3,3),
                     padding='same',
                     input_shape=(160,160,3),
                     activation='relu'))

    # Create Max-Pool 2
    model.add(MaxPooling2D(pool_size=(2,2)))

    # Add Dropout layer
    model.add(Dropout(0.25))

    #DNN
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(4, activation='softmax'))

    model.load_weights(KERAS_MODEL_WEIG)

    model.summary()

    gray = cv2.imread('bird_binary.jpg')
    test = cv2.resize(gray,(160,160),interpolation=cv2.INTER_CUBIC).reshape(1, 160, 160, 3).astype('float32')
    test_norm = test/255
    model.predict_classes(test_norm)

def run():
    label = {0:u'no img!',1:u'scissors',2:u'stone',3:u'paper'}
    
    cap = cv2.VideoCapture('http://127.0.0.1:8080/?action=stream?dummy=param.mjpg')
    # 設定影像尺寸
    cap.set(3,320)
    cap.set(4,240)
    while True:
        ret, frame = cap.read()
        if ret:
            height, width = frame.shape[:2]
            test = cv2.resize(frame[80:240,60:220],(160,160),interpolation=cv2.INTER_CUBIC).reshape(1, 160, 160, 3).astype('float32')
            test_norm = test/255
            labelType = model.predict_classes(test_norm)[0]
            cv2.putText(frame,label[labelType],(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1,cv2.LINE_AA) 
            cv2.imshow('cam',frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                cap.release()
                break
            
if __name__ == "__main__":
    dnnInit()
    run()
