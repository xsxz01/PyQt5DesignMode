from PyQt5.QtWidgets import QMainWindow

import UI_MainWindow
from Generator import Generator
from Insert_Dialog import Insert_Dialog
from Mutiple_dialog import Muitiple_Dialog
from RunDialog import RunDialog
from Simple_Dialog import Simple_Dialog


class MainWindow(QMainWindow, UI_MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # 连接所有按钮事件
        self.pushButton_run.clicked.connect(self.clicked_button_run)
        self.pushButton_simple.clicked.connect(self.clicked_button_simple)
        self.pushButton_multiple.clicked.connect(self.clicked_button_mutiple)
        self.pushButton_insert.clicked.connect(self.clicked_button_insert)

    def clicked_button_run(self):
        self.run = RunDialog()
        self.run.show()

    def clicked_button_simple(self):
        self.simple = Simple_Dialog()
        self.simple.show()

    def clicked_button_mutiple(self):
        self.multiple = Muitiple_Dialog()
        self.multiple.show()

    def clicked_button_insert(self):
        self.insert = Insert_Dialog()
        self.insert.show()