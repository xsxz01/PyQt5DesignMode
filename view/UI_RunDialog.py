# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_RunDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Run_Dialog(object):
    def setupUi(self, Run_Dialog):
        Run_Dialog.setObjectName("Run_Dialog")
        Run_Dialog.resize(1064, 918)
        self.layoutWidget = QtWidgets.QWidget(Run_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 701, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.pushButton_start = QtWidgets.QPushButton(Run_Dialog)
        self.pushButton_start.setGeometry(QtCore.QRect(780, 20, 251, 81))
        self.pushButton_start.setStyleSheet("background-color:#FFFFFF;\n"
"height:40px;\n"
"font: 25 18pt \"等线 Light\";\n"
"border:1px solid #00FF00;\n"
"border-radius:25px;")
        self.pushButton_start.setObjectName("pushButton_start")
        self.label_cap = QtWidgets.QLabel(Run_Dialog)
        self.label_cap.setGeometry(QtCore.QRect(120, 100, 800, 800))
        self.label_cap.setText("")
        self.label_cap.setObjectName("label_cap")
        self.layoutWidget1 = QtWidgets.QWidget(Run_Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 701, 35))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMaximumSize(QtCore.QSize(137, 16777215))
        self.label.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setMaximumSize(QtCore.QSize(137, 16777215))
        self.label_9.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setStyleSheet("font: 25 18pt \"等线 Light\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Run_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Run_Dialog)

    def retranslateUi(self, Run_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Run_Dialog.setWindowTitle(_translate("Run_Dialog", "开始考勤"))
        self.label_3.setText(_translate("Run_Dialog", "应到："))
        self.label_4.setText(_translate("Run_Dialog", "~人"))
        self.label_5.setText(_translate("Run_Dialog", "实到："))
        self.label_6.setText(_translate("Run_Dialog", "~人"))
        self.label_7.setText(_translate("Run_Dialog", "未到："))
        self.label_8.setText(_translate("Run_Dialog", "~人"))
        self.pushButton_start.setText(_translate("Run_Dialog", "开始"))
        self.label.setText(_translate("Run_Dialog", "考勤状态："))
        self.label_2.setText(_translate("Run_Dialog", "未开始"))
        self.label_9.setText(_translate("Run_Dialog", "考勤次数："))
        self.label_10.setText(_translate("Run_Dialog", "未开始"))
