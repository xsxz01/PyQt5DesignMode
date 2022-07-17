from PyQt5.QtWidgets import QMainWindow

import UI_Generator


class Generator(UI_Generator.Ui_Generator_Dialog, QMainWindow):
    def __init__(self):
        super(UI_Generator.Ui_Generator_Dialog, self).__init__()
        self.setupUi(self)