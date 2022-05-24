from PyQt5.QtWidgets import QMainWindow, QMessageBox

import UI_MainWindow
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
        self.pushButton_simple.setHidden(True)
        self.pushButton_multiple.clicked.connect(self.clicked_button_mutiple)
        self.pushButton_multiple.setHidden(True)
        self.pushButton_insert.clicked.connect(self.clicked_button_insert)
        self.pushButton_train.setHidden(True)

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

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告', '<font size=16 face='+'等线 Light'+' color=red><b>窗口关闭后，将终止本次运行</b></font>',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # 依次关闭所有窗口
            self.insert.close()
            self.simple.close()
            self.run.close()
            self.multiple.close()
            event.accept()
        else:
            event.ignore()

