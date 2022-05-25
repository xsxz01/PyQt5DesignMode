from PyQt5.QtWidgets import QMainWindow
import UI_KaoQin_Dialog


class KaoQin_Dialog(UI_KaoQin_Dialog.Ui_KaoQin_Dialog, QMainWindow):
    def __init__(self):
        super(UI_KaoQin_Dialog.Ui_KaoQin_Dialog, self).__init__()
        self.setupUi(self)