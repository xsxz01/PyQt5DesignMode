from PyQt5.QtWidgets import QMainWindow

import UI_Simple_Dialog


class Simple_Dialog(UI_Simple_Dialog.Ui_Simple_Dialog, QMainWindow):
    def __init__(self):
        super(UI_Simple_Dialog.Ui_Simple_Dialog, self).__init__()
        self.setupUi(self)