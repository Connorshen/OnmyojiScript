# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\billshen\Documents\GitHub\OnmyojiScript\view\design\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 777)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QHBoxLayout()
        self.top.setObjectName("top")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.video_lb = QtWidgets.QLabel(self.centralwidget)
        self.video_lb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.video_lb.setObjectName("video_lb")
        self.verticalLayout_2.addWidget(self.video_lb)
        self.top.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.recognition_lb = QtWidgets.QLabel(self.centralwidget)
        self.recognition_lb.setObjectName("recognition_lb")
        self.verticalLayout_5.addWidget(self.recognition_lb)
        self.top.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.top)
        self.info = QtWidgets.QGridLayout()
        self.info.setObjectName("info")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.left_lb = QtWidgets.QLabel(self.centralwidget)
        self.left_lb.setText("")
        self.left_lb.setObjectName("left_lb")
        self.gridLayout.addWidget(self.left_lb, 0, 1, 1, 1)
        self.right_lb = QtWidgets.QLabel(self.centralwidget)
        self.right_lb.setText("")
        self.right_lb.setObjectName("right_lb")
        self.gridLayout.addWidget(self.right_lb, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.height_lb = QtWidgets.QLabel(self.centralwidget)
        self.height_lb.setText("")
        self.height_lb.setObjectName("height_lb")
        self.gridLayout.addWidget(self.height_lb, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.width_lb = QtWidgets.QLabel(self.centralwidget)
        self.width_lb.setText("")
        self.width_lb.setObjectName("width_lb")
        self.gridLayout.addWidget(self.width_lb, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.scene_lb = QtWidgets.QLabel(self.centralwidget)
        self.scene_lb.setText("")
        self.scene_lb.setObjectName("scene_lb")
        self.gridLayout.addWidget(self.scene_lb, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.bottom_lb = QtWidgets.QLabel(self.centralwidget)
        self.bottom_lb.setText("")
        self.bottom_lb.setObjectName("bottom_lb")
        self.gridLayout.addWidget(self.bottom_lb, 3, 1, 1, 1)
        self.top_lb = QtWidgets.QLabel(self.centralwidget)
        self.top_lb.setText("")
        self.top_lb.setObjectName("top_lb")
        self.gridLayout.addWidget(self.top_lb, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.is_running_lb = QtWidgets.QLabel(self.centralwidget)
        self.is_running_lb.setText("")
        self.is_running_lb.setObjectName("is_running_lb")
        self.gridLayout.addWidget(self.is_running_lb, 7, 1, 1, 1)
        self.info.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.reg_template_lb = QtWidgets.QLabel(self.verticalGroupBox)
        self.reg_template_lb.setText("")
        self.reg_template_lb.setObjectName("reg_template_lb")
        self.verticalLayout_3.addWidget(self.reg_template_lb)
        self.gridLayout_2.addWidget(self.verticalGroupBox, 0, 0, 1, 1)
        self.info.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout.addWidget(self.start_btn)
        self.end_btn = QtWidgets.QPushButton(self.centralwidget)
        self.end_btn.setObjectName("end_btn")
        self.horizontalLayout.addWidget(self.end_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "护肝神器"))
        self.label.setText(_translate("MainWindow", "捕获"))
        self.video_lb.setText(_translate("MainWindow", "Video"))
        self.label_4.setText(_translate("MainWindow", "识别结果"))
        self.recognition_lb.setText(_translate("MainWindow", "Recognition Result"))
        self.label_5.setText(_translate("MainWindow", "Scene"))
        self.label_8.setText(_translate("MainWindow", "Bottom"))
        self.label_3.setText(_translate("MainWindow", "Top"))
        self.label_2.setText(_translate("MainWindow", "Left"))
        self.label_7.setText(_translate("MainWindow", "Height"))
        self.label_6.setText(_translate("MainWindow", "Right"))
        self.label_10.setText(_translate("MainWindow", "Width"))
        self.label_9.setText(_translate("MainWindow", "脚本运行状态"))
        self.verticalGroupBox.setTitle(_translate("MainWindow", "识别出的模板"))
        self.start_btn.setText(_translate("MainWindow", "开始脚本"))
        self.end_btn.setText(_translate("MainWindow", "结束"))
