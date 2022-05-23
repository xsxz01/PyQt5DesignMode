# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 596)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 80, 441, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 36pt \"黑体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton_insert = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_insert.setStyleSheet("background-color:#FFFFFF;\n"
"height:40px;\n"
"font: 25 18pt \"等线 Light\";\n"
"border:1px solid #00FF00;\n"
"border-radius:25px;")
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.verticalLayout.addWidget(self.pushButton_insert)
        self.pushButton_train = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_train.setStyleSheet("background-color:#FFFFFF;\n"
"height:40px;\n"
"font: 25 18pt \"等线 Light\";\n"
"border:1px solid #00FF00;\n"
"border-radius:25px;")
        self.pushButton_train.setObjectName("pushButton_train")
        self.verticalLayout.addWidget(self.pushButton_train)
        self.pushButton_run = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_run.setStyleSheet("background-color:#FFFFFF;\n"
"height:40px;\n"
"font: 25 18pt \"等线 Light\";\n"
"border:1px solid #00FF00;\n"
"border-radius:25px;")
        self.pushButton_run.setObjectName("pushButton_run")
        self.verticalLayout.addWidget(self.pushButton_run)
        self.pushButton_simple = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_simple.setStyleSheet("background-color:#FFFFFF;\n"
"height:40px;\n"
"font: 25 18pt \"等线 Light\";\n"
"border:1px solid #00FF00;\n"
"border-radius:25px;")
        self.pushButton_simple.setObjectName("pushButton_simple")
        self.verticalLayout.addWidget(self.pushButton_simple)
        self.pushButton_multiple = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_multiple.setStyleSheet("background-color:#FFFFFF;\n"
"height:40px;\n"
"font: 25 18pt \"等线 Light\";\n"
"border:1px solid #00FF00;\n"
"border-radius:25px;")
        self.pushButton_multiple.setObjectName("pushButton_multiple")
        self.verticalLayout.addWidget(self.pushButton_multiple)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "考勤"))
        self.label.setText(_translate("MainWindow", "主界面"))
        self.pushButton_insert.setText(_translate("MainWindow", "录入数据"))
        self.pushButton_train.setText(_translate("MainWindow", "训练数据"))
        self.pushButton_run.setText(_translate("MainWindow", "开始考勤"))
        self.pushButton_simple.setText(_translate("MainWindow", "单人考勤"))
        self.pushButton_multiple.setText(_translate("MainWindow", "多人考勤"))
import testRes_rc
