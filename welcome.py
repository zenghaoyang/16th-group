# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '欢迎使用.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(751, 519)
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
"QWidget {\n"
"border-image:url(C:/Users/123/Desktop/ruangong/MaskDetect-YOLOv4-PyTorch-master/pyqt5/背景.jpeg);\n"
"}\n"
"\n"
"#下面的防止背景干扰其他控件\n"
"QTextBrowser {\n"
"border-image:url();\n"
"}\n"
"QLineEdit {\n"
"border-image:url();\n"
"}\n"
"QComboBox {\n"
"border-image:url();\n"
"}\n"
"QLabel {\n"
"border-image:url();\n"
"}\n"
"QPushButton {\n"
"border-image:url();\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(50, 280, 231, 51))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(12)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(50, 400, 231, 51))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(12)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(480, 280, 231, 51))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(12)
        font.setUnderline(False)
        self.btn3.setFont(font)
        self.btn3.setFlat(False)
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(480, 400, 231, 51))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(12)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.textlabel = QtWidgets.QLabel(self.centralwidget)
        self.textlabel.setGeometry(QtCore.QRect(160, 70, 451, 81))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.textlabel.setFont(font)
        self.textlabel.setObjectName("textlabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "16小组口罩识别系统"))
        self.btn1.setText(_translate("MainWindow", "摄像头拍照检测"))
        self.btn2.setText(_translate("MainWindow", "摄像头实时检测"))
        self.btn3.setText(_translate("MainWindow", "本地照片检测"))
        self.btn4.setText(_translate("MainWindow", "本地视频检测"))
        self.textlabel.setText(_translate("MainWindow", "欢迎使用，请选择你要使用的功能哦~"))
        self.action1.setText(_translate("MainWindow", "摄像头实时检测"))
        self.action2.setText(_translate("MainWindow", "摄像头拍照检测"))
        self.action3.setText(_translate("MainWindow", "本地照片检测"))
        self.action_4.setText(_translate("MainWindow", "本地视频检测"))
        