# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_User_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_User_Dialog(object):
    def setupUi(self, User_Dialog):
        User_Dialog.setObjectName("User_Dialog")
        User_Dialog.resize(1061, 749)
        self.layoutWidget = QtWidgets.QWidget(User_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 10, 991, 711))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 28pt \"黑体\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(195)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(User_Dialog)
        QtCore.QMetaObject.connectSlotsByName(User_Dialog)

    def retranslateUi(self, User_Dialog):
        _translate = QtCore.QCoreApplication.translate
        User_Dialog.setWindowTitle(_translate("User_Dialog", "Dialog"))
        self.label.setText(_translate("User_Dialog", "用户数据"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("User_Dialog", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("User_Dialog", "名字"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("User_Dialog", "学号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("User_Dialog", "院系"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("User_Dialog", "操作"))