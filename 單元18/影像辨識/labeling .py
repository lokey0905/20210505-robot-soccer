import cv2
import sys
import ctypes
import time
import json

from PySide.QtGui import QMainWindow,QApplication,QPixmap,QImage
from PySide.QtCore import Signal,QThread

import gui

SYS_CLOSE = False
VIDEO_INDEX = 0

cap = cv2.VideoCapture('video.avi')

class sample(QThread):
    changePixmap = Signal(QImage)
    def __init__(self):
        super(self.__class__, self).__init__()
        
    def run(self):
        global SYS_CLOSE,VIDEO_INDEX
        while 1:
            frame = cv2.imread('./samples_cut/' + str(VIDEO_INDEX) + '.jpg')
            frame = cv2.resize(frame,(640,480),interpolation=cv2.INTER_CUBIC)
            height, width = frame.shape[:2]
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            ch = ctypes.c_char.from_buffer(rgbImage)
            rcount = ctypes.c_long.from_address(id(ch)).value
            rgbImage = QImage(ch,width,height,width * 3, QImage.Format_RGB888)
            self.changePixmap.emit(rgbImage)
            ctypes.c_long.from_address(id(ch)).value = rcount
            time.sleep(.2)
            if SYS_CLOSE:
                cap.release()
                break
    
class Main(QMainWindow,gui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)   
        self.lastLabel = [0,0]

        name = 0

        ret,frame = cap.read()
        while ret:
            cv2.imwrite('./samples_cut/' + str(name) + '.jpg',frame[200:,50:590])
                
            name += 1
            ret,frame = cap.read()
                
        self.Labels = [0] * name
        self.totalClass = {"":0}
        self.classIndex = 1
        self.timeSlider.setMaximum(name-1)
        self.sample = sample()
        self.sample.changePixmap.connect(self.sampleSetImage)
        self.sample.start()
        
        self.textEdit.append('開始標記：')
        
    def bgClick(self):
        self.labelSet(self.lastLabel[1],self.timeSlider.value(),0)
        self.textEdit.append('\n'+ str(self.lastLabel[1]) + '至' + 
                             str(self.timeSlider.value()) + '標為0（無圖樣）')
        self.lastLabel = [0,self.timeSlider.value() + 1]

    def l1Click(self):
        if self.lineEdit.text() not in self.totalClass:
            self.totalClass[self.lineEdit.text()] = self.classIndex
            self.classIndex += 1
        self.labelSet(self.lastLabel[1],self.timeSlider.value(),self.totalClass[self.lineEdit.text()])
        showText = '\n'+ str(self.lastLabel[1]) + '至' + str(self.timeSlider.value()) + '標為'
        self.textEdit.append(showText + self.lineEdit.text() if self.lineEdit.text() != "" else showText + '無物體')
        self.lastLabel = [self.totalClass[self.lineEdit.text()],self.timeSlider.value() + 1]

    def labelSet(self,start,end,label):
        for i in range(start,end+1):self.Labels[i] = label
        
    def timeChange(self):
        global VIDEO_INDEX
        VIDEO_INDEX = self.timeSlider.value()
        self.timeLabel.setText(str(VIDEO_INDEX))

    def sampleSetImage(self,image):
        self.picLabel.setPixmap(QPixmap.fromImage(image))
            
    def closeEvent(self, event):
        global SYS_CLOSE,cap
        SYS_CLOSE = True
        with open('label.txt','w') as f:
            json.dump(self.Labels,f)
        with open('labelName.txt','w') as f:
            json.dump({int(v): k for k, v in self.totalClass.items()},f)
        event.accept()  
                
if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance() 
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())