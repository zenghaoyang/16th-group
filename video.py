# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '本地视频识别.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labresult4 = QtWidgets.QLabel(self.centralwidget)
        self.labresult4.setObjectName("labresult4")
        self.gridLayout.addWidget(self.labresult4, 0, 0, 1, 1)
        self.btnopenfile = QtWidgets.QPushButton(self.centralwidget)
        self.btnopenfile.setStyleSheet("QPushButton\n"
"{\n"
"background-color:blue;\n"
"color:#ffffff\n"
"font:75 13pt \"宋体\"\n"
"}")
        self.btnopenfile.setObjectName("btnopenfile")
        self.gridLayout.addWidget(self.btnopenfile, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 751, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action3)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.btnopenfile.clicked.connect(MainWindow.btnopenvideo_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "16小组口罩识别系统"))
        self.labresult4.setText(_translate("MainWindow", "                                 结 果 视 频"))
        self.btnopenfile.setText(_translate("MainWindow", "选 择 本 地 视 频"))
        self.menu.setTitle(_translate("MainWindow", "模式切换"))
        self.action1.setText(_translate("MainWindow", "摄像头实时检测"))
        self.action2.setText(_translate("MainWindow", "摄像头拍照检测"))
        self.action3.setText(_translate("MainWindow", "本地照片检测"))
        self.action_4.setText(_translate("MainWindow", "本地视频检测"))
