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
        self.verticalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recognition_lb = QtWidgets.QLabel(self.verticalGroupBox)
        self.recognition_lb.setObjectName("recognition_lb")
        self.verticalLayout_2.addWidget(self.recognition_lb)
        self.top.addWidget(self.verticalGroupBox)
        self.verticalGroupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox1.setObjectName("verticalGroupBox1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.video_info = QtWidgets.QGridLayout()
        self.video_info.setObjectName("video_info")
        self.left_lb = QtWidgets.QLabel(self.verticalGroupBox1)
        self.left_lb.setText("")
        self.left_lb.setObjectName("left_lb")
        self.video_info.addWidget(self.left_lb, 0, 1, 1, 1)
        self.right_lb = QtWidgets.QLabel(self.verticalGroupBox1)
        self.right_lb.setText("")
        self.right_lb.setObjectName("right_lb")
        self.video_info.addWidget(self.right_lb, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalGroupBox1)
        self.label_5.setObjectName("label_5")
        self.video_info.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalGroupBox1)
        self.label_8.setObjectName("label_8")
        self.video_info.addWidget(self.label_8, 3, 0, 1, 1)
        self.height_lb = QtWidgets.QLabel(self.verticalGroupBox1)
        self.height_lb.setText("")
        self.height_lb.setObjectName("height_lb")
        self.video_info.addWidget(self.height_lb, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalGroupBox1)
        self.label_3.setObjectName("label_3")
        self.video_info.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox1)
        self.label_2.setObjectName("label_2")
        self.video_info.addWidget(self.label_2, 0, 0, 1, 1)
        self.width_lb = QtWidgets.QLabel(self.verticalGroupBox1)
        self.width_lb.setText("")
        self.width_lb.setObjectName("width_lb")
        self.video_info.addWidget(self.width_lb, 5, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalGroupBox1)
        self.label_7.setObjectName("label_7")
        self.video_info.addWidget(self.label_7, 4, 0, 1, 1)
        self.scene_lb = QtWidgets.QLabel(self.verticalGroupBox1)
        self.scene_lb.setText("")
        self.scene_lb.setObjectName("scene_lb")
        self.video_info.addWidget(self.scene_lb, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalGroupBox1)
        self.label_6.setObjectName("label_6")
        self.video_info.addWidget(self.label_6, 2, 0, 1, 1)
        self.bottom_lb = QtWidgets.QLabel(self.verticalGroupBox1)
        self.bottom_lb.setText("")
        self.bottom_lb.setObjectName("bottom_lb")
        self.video_info.addWidget(self.bottom_lb, 3, 1, 1, 1)
        self.top_lb = QtWidgets.QLabel(self.verticalGroupBox1)
        self.top_lb.setText("")
        self.top_lb.setObjectName("top_lb")
        self.video_info.addWidget(self.top_lb, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalGroupBox1)
        self.label_10.setObjectName("label_10")
        self.video_info.addWidget(self.label_10, 5, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalGroupBox1)
        self.label_9.setObjectName("label_9")
        self.video_info.addWidget(self.label_9, 7, 0, 1, 1)
        self.is_running_lb = QtWidgets.QLabel(self.verticalGroupBox1)
        self.is_running_lb.setText("")
        self.is_running_lb.setObjectName("is_running_lb")
        self.video_info.addWidget(self.is_running_lb, 7, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.video_info)
        self.top.addWidget(self.verticalGroupBox1)
        self.verticalLayout.addLayout(self.top)
        self.verticalGroupBox2 = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox2.setObjectName("verticalGroupBox2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalGroupBox2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.verticalGroupBox2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.verticalGroupBox2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.config_token_et = QtWidgets.QLineEdit(self.verticalGroupBox2)
        self.config_token_et.setObjectName("config_token_et")
        self.gridLayout.addWidget(self.config_token_et, 1, 1, 1, 1)
        self.excution_times_sb = QtWidgets.QSpinBox(self.verticalGroupBox2)
        self.excution_times_sb.setMinimum(1)
        self.excution_times_sb.setObjectName("excution_times_sb")
        self.gridLayout.addWidget(self.excution_times_sb, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalGroupBox2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.verticalGroupBox2)
        self.info = QtWidgets.QGridLayout()
        self.info.setObjectName("info")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalGroupBox3 = QtWidgets.QGroupBox(self.centralwidget)
        self.verticalGroupBox3.setObjectName("verticalGroupBox3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalGroupBox3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.reg_template_lb = QtWidgets.QLabel(self.verticalGroupBox3)
        self.reg_template_lb.setText("")
        self.reg_template_lb.setObjectName("reg_template_lb")
        self.verticalLayout_3.addWidget(self.reg_template_lb)
        self.log_lv = QtWidgets.QListWidget(self.verticalGroupBox3)
        self.log_lv.setObjectName("log_lv")
        self.verticalLayout_3.addWidget(self.log_lv)
        self.gridLayout_2.addWidget(self.verticalGroupBox3, 0, 0, 1, 1)
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
        self.about_btn = QtWidgets.QAction(MainWindow)
        self.about_btn.setObjectName("about_btn")
        self.config_btn = QtWidgets.QAction(MainWindow)
        self.config_btn.setObjectName("config_btn")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "护肝神器"))
        self.verticalGroupBox.setTitle(_translate("MainWindow", "识别图像"))
        self.recognition_lb.setText(_translate("MainWindow", "Recognition Result"))
        self.verticalGroupBox1.setTitle(_translate("MainWindow", "状态信息"))
        self.label_5.setText(_translate("MainWindow", "场景"))
        self.label_8.setText(_translate("MainWindow", "Bottom"))
        self.label_3.setText(_translate("MainWindow", "Top"))
        self.label_2.setText(_translate("MainWindow", "Left"))
        self.label_7.setText(_translate("MainWindow", "高度"))
        self.label_6.setText(_translate("MainWindow", "Right"))
        self.label_10.setText(_translate("MainWindow", "宽度"))
        self.label_9.setText(_translate("MainWindow", "脚本运行状态"))
        self.verticalGroupBox2.setTitle(_translate("MainWindow", "配置"))
        self.label_11.setText(_translate("MainWindow", "关注瞎推啥公众号，获取Token，填入下面这个输入框。脚本运行结束之后会往手机微信上发通知。"))
        self.label_4.setText(_translate("MainWindow", "刷几次(建议30次以下)"))
        self.label.setText(_translate("MainWindow", "虾推啥Token(填自己的，不要用我的)"))
        self.verticalGroupBox3.setTitle(_translate("MainWindow", "识别出的模板"))
        self.start_btn.setText(_translate("MainWindow", "开始脚本（F1）"))
        self.end_btn.setText(_translate("MainWindow", "结束（F12）"))
        self.about_btn.setText(_translate("MainWindow", "关于"))
        self.config_btn.setText(_translate("MainWindow", "软件设置"))
