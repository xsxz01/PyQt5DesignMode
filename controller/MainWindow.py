from PyQt5.QtWidgets import QMainWindow, QMessageBox

from view import UI_MainWindow

from controller.Insert_Dialog import Insert_Dialog
from controller.KaoQin_Dialog import KaoQin_Dialog
from controller.Mutiple_dialog import Muitiple_Dialog
from controller.RunDialog import RunDialog
from controller.User_Dialog import User_Dialog


class MainWindow(QMainWindow, UI_MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 连接所有按钮事件
        self.pushButton_run.clicked.connect(self.clicked_button_run)
        self.pushButton_simple.clicked.connect(self.clicked_button_simple)
        # self.pushButton_simple.setHidden(True)
        self.pushButton_multiple.clicked.connect(self.clicked_button_mutiple)
        self.pushButton_multiple.setHidden(True)
        self.pushButton_insert.clicked.connect(self.clicked_button_insert)
        # self.pushButton_train.setHidden(True)
        self.pushButton_train.clicked.connect(self.clicked_button_train)

    def clicked_button_run(self):
        self.run = RunDialog()
        self.run.show()

    def clicked_button_simple(self):
        self.training = KaoQin_Dialog()
        self.training.show()
        # self.simple = Simple_Dialog()
        # self.simple.show()

    def clicked_button_mutiple(self):
        self.multiple = Muitiple_Dialog()
        self.multiple.show()

    def clicked_button_insert(self):
        self.insert = Insert_Dialog()
        self.insert.show()

    def clicked_button_train(self):
        self.training = User_Dialog()
        self.training.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告',
                                     '<font size=16 face=' + '等线 Light' + ' color=red><b>窗口关闭后，将终止本次运行</b></font>',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # 依次关闭所有窗口
            if self.insert:
                self.insert.close()
            if self.simple:
                self.simple.close()
            if self.run:
                self.run.close()
            if self.multiple:
                self.multiple.close()
            event.accept()
        else:
            event.ignore()
