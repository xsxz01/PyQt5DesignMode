from PyQt5.QtWidgets import QMainWindow

import UI_RunDialog


class RunDialog(UI_RunDialog.Ui_Run_Dialog, QMainWindow):
    def __init__(self):
        super(UI_RunDialog.Ui_Run_Dialog, self).__init__()
        self.setupUi(self)