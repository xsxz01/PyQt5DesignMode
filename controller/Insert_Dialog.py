from PyQt5.QtWidgets import QMainWindow

import UI_Simple_Dialog
import UI_Insert_Dialog


class Insert_Dialog(UI_Insert_Dialog.Ui_Insert_Dialog, QMainWindow):
    def __init__(self):
        super(UI_Insert_Dialog.Ui_Insert_Dialog, self).__init__()
        self.setupUi(self)