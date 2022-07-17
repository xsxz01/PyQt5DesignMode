from PyQt5.QtWidgets import QMainWindow

import UI_MainWindow
from Generator import Generator


class MainWindow(QMainWindow, UI_MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.clicked_button_login)

    def clicked_button_login(self):
        print("打开第二个窗口")
        self.generator = Generator()
        self.generator.show()