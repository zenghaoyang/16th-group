import sys
import cv2
import time
import numpy as np
from yolo import YOLO
import cv2 as cv
from PIL import Image, ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from welcome import Ui_MainWindow as zero_Ui
from camerashot import Ui_MainWindow as one_Ui
from cameratime import Ui_MainWindow as two_Ui
from picture import Ui_MainWindow as three_Ui
from video import Ui_MainWindow as four_Ui

# 主窗口
class Welcome(QtWidgets.QMainWindow, zero_Ui):
    switch_window1 = QtCore.pyqtSignal() # 跳转信号
    switch_window2 = QtCore.pyqtSignal() # 跳转信号
    switch_window3 = QtCore.pyqtSignal() # 跳转信号
    switch_window4 = QtCore.pyqtSignal() # 跳转信号
    
    def __init__(self):
        super(Welcome, self).__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.goOne)
        self.btn2.clicked.connect(self.goTwo)
        self.btn3.clicked.connect(self.goThree)
        self.btn4.clicked.connect(self.goFour)
        op1 = QtWidgets.QGraphicsOpacityEffect()# 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op1.setOpacity(0.6)
        self.btn1.setGraphicsEffect(op1)
        op2 = QtWidgets.QGraphicsOpacityEffect()
        op2.setOpacity(0.6)
        self.btn2.setGraphicsEffect(op2)
        op3 = QtWidgets.QGraphicsOpacityEffect()
        op3.setOpacity(0.6)
        self.btn3.setGraphicsEffect(op3)
        op4 = QtWidgets.QGraphicsOpacityEffect()
        op4.setOpacity(0.6)
        self.btn4.setGraphicsEffect(op4)
        
    def goOne(self):
        self.switch_window1.emit()
    def goTwo(self):
        self.switch_window2.emit()
    def goThree(self):
        self.switch_window3.emit()
    def goFour(self):
        self.switch_window4.emit()


class Camerashot(QMainWindow, one_Ui):
    def __init__(self):
        super(Camerashot, self).__init__()
        self.setupUi(self)
        self.camera = cv.VideoCapture(0)
        self.is_camera_opened = False  # 摄像头有没有打开标记

        # 定时器：30ms捕获一帧
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(90)
        
    def btnopencamera_Clicked(self):
        '''
        打开和关闭摄像头
        '''
        self.is_camera_opened = ~self.is_camera_opened
        if self.is_camera_opened:
            self.btnopencamera.setText("关闭摄像头")
            self._timer.start()
        else:
            self.btnopencamera.setText("打开摄像头")
            self._timer.stop()

    def btnshot_Clicked(self):
        '''
        捕获图片
        '''
        # 摄像头未打开，不执行任何操作
        if not self.is_camera_opened:
            return

        self.captured = self.frame

        # 后面这几行代码几乎都一样，可以尝试封装成一个函数
        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        # Qt显示图片时，需要先转换成QImgage类型
        QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
        self.labshot.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labshot.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    
    def btnresult_Clicked(self):
        yolo = YOLO()
        '''
        显示结果
        '''
        # 如果没有捕获图片，则不执行操作
        if not hasattr(self, "captured"):
            return

        rows, cols, channels = self.captured.shape
        bytesPerLine = channels * cols
        # Qt显示图片时，需要先转换成QImgage类型
        QImg = QImage(self.captured.data, cols, rows, bytesPerLine, QImage.Format_RGB888)
        image = ImageQt.fromqimage(QImg)
        image = yolo.detect_image(image)
        QImg = ImageQt.ImageQt(image)
        self.labresult.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labresult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

   
    @QtCore.pyqtSlot()
    def _queryFrame(self):
        '''
        循环捕获图片
        '''
        ret, self.frame = self.camera.read()

        img_rows, img_cols, channels = self.frame.shape
        bytesPerLine = channels * img_cols

        cv.cvtColor(self.frame, cv.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888)
        self.labcamera.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labcamera.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

class Cameratime(QtWidgets.QMainWindow, two_Ui):
    def __init__(self):
        super(Cameratime, self).__init__()
        self.setupUi(self)
        self.camera = cv.VideoCapture(0)
        self.is_camera_opened = False  # 摄像头有没有打开标记

        # 定时器：30ms捕获一帧
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(30)
        
    def btnopencamera2_Clicked(self):
        '''
        打开和关闭摄像头
        '''
        self.is_camera_opened = ~self.is_camera_opened
        if self.is_camera_opened:
            self.btnopencamera2.setText("停止识别")
            self._timer.start()
        else:
            self.btnopencamera2.setText("打开摄像头")
            self._timer.stop()
        #实时刷新界面
        QtWidgets.QApplication.processEvents()
        #睡眠0.05秒
        time.sleep(0.05)
    @QtCore.pyqtSlot()
    def _queryFrame(self):
        yolo = YOLO()
        '''
        循环捕获图片
        '''
        ret, self.frame = self.camera.read()
        img_rows, img_cols, channels = self.frame.shape
        bytesPerLine = channels * img_cols
        cv.cvtColor(self.frame, cv.COLOR_BGR2RGB, self.frame)
        QImg = QImage(self.frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888) 
        image = ImageQt.fromqimage(QImg)
        image = yolo.detect_image(image)
        QImg = ImageQt.ImageQt(image)
        self.labresult2.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labresult2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

class Picture(QtWidgets.QMainWindow, three_Ui):
    def __init__(self):
        super(Picture, self).__init__()
        self.setupUi(self)
    def btnopenpicture_Clicked(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'img/', 'Image files(*.jpg *.gif *.png)')  # 从本地选一张图片
        image = Image.open(fname)
        yolo = YOLO()
        # 加载模型，将image送进模型
        image = yolo.detect_image(image)
        QImg = ImageQt.ImageQt(image)
        self.labresult3.setPixmap(QPixmap.fromImage(QImg).scaled(
            self.labresult3.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        
class Video(QtWidgets.QMainWindow, four_Ui):
    def __init__(self):
        super(Video, self).__init__()
        self.setupUi(self)
        
    def btnopenvideo_Clicked(self):
        yolo = YOLO()
        fname, _ = QFileDialog.getOpenFileName(self, '选择视频', 'video/', 'Video files(*.mp4 *.avi )')  # 从本地选一个视频文件
        capture = cv2.VideoCapture(fname)
        fps = 0.0
        while True:
            t1 = time.time()
            # 读取某一帧
            grabbed, frame = capture.read()
            if not grabbed:
                break
            img_rows, img_cols, channels = frame.shape
            bytesPerLine = channels * img_cols
        # opencv读取的是BGR，格式转变，BGRtoRGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 转变成Image
            frame = Image.fromarray(np.uint8(frame))
        # 进行检测
            frame = np.array(yolo.detect_image(frame))
         # RGBtoBGR满足opencv显示格式
            frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            QImg = QImage(frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888)
            self.labresult4.setPixmap(QPixmap.fromImage(QImg).scaled(self.labresult4.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            fps  = (fps + (1. / (time.time() - t1))) / 2
            print("FPS: %.2f" % (fps))
            frame = cv2.putText(frame, "FPS: %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv.cvtColor(frame, cv.COLOR_BGR2RGB, frame)    
            QImg = QImage(frame.data, img_cols, img_rows, bytesPerLine, QImage.Format_RGB888)
            self.labresult4.setPixmap(QPixmap.fromImage(QImg).scaled(self.labresult4.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            #实时刷新界面
            QtWidgets.QApplication.processEvents()
            #睡眠0.05秒
            time.sleep(0.05)
            #if writer is None:
                #fourcc = cv2.VideoWriter_fourcc(*'MP4V')
                #writer = cv2.VideoWriter(fname.split('.')[0] + '_result.mp4', fourcc, 30, (frame.shape[1], frame.shape[0]), True)
            #writer.write(frame)
        #writer.release()
        #capture.release()
        
# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass
    # 跳转到 zero 窗口
    def show_zero(self):
        self.zero = Welcome()
        self.zero.switch_window1.connect(self.show_one)
        self.zero.switch_window2.connect(self.show_two)
        self.zero.switch_window3.connect(self.show_three)
        self.zero.switch_window4.connect(self.show_four)
        self.zero.show()
    # 跳转到 one 窗口, 注意关闭原页面
    def show_one(self):
        self.one = Camerashot()
        self.zero.close()
        self.one.show()
    # 跳转到 two 窗口, 注意关闭原页面
    def show_two(self):
        self.two = Cameratime()
        self.zero.close()
        self.two.show()
    # 跳转到 three 窗口, 注意关闭原页面
    def show_three(self):
        self.three = Picture()
        self.zero.close()
        self.three.show()
    # 跳转到 four 窗口, 注意关闭原页面
    def show_four(self):
        self.four = Video()
        self.zero.close()
        self.four.show()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('mask.jpeg'))
    controller = Controller() # 控制器实例
    controller.show_zero() # 默认展示的是 zero 页面
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()