import sys
import cv2 as cv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow

from mainForm import Ui_MainWindow


class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.camera = cv.VideoCapture(0)
        self.is_camera_opened = False  # 摄像头有没有打开标记

        # 定时器：30ms捕获一帧
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(30)

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
        '''
        灰度化
        '''
        # 如果没有捕获图片，则不执行操作
        if not hasattr(self, "captured"):
            return

        self.cpatured = cv.cvtColor(self.captured, cv.COLOR_RGB2GRAY)

        rows, columns = self.cpatured.shape
        bytesPerLine = columns
        # 灰度图是单通道，所以需要用Format_Indexed8
        QImg = QImage(self.cpatured.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec_())