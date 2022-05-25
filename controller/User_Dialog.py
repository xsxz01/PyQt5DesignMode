from PyQt5.QtWidgets import QMainWindow
import UI_User_Dialog


class User_Dialog(UI_User_Dialog.Ui_User_Dialog, QMainWindow):
    def __init__(self):
        super(UI_User_Dialog.Ui_User_Dialog, self).__init__()
        self.setupUi(self)