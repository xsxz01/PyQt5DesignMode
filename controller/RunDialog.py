from PyQt5.QtWidgets import QMainWindow

import UI_RunDialog
import config
import face_recognition


class RunDialog(UI_RunDialog.Ui_Run_Dialog, QMainWindow):
    def __init__(self):
        super(UI_RunDialog.Ui_Run_Dialog, self).__init__()
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.start)
        # 生成轮次参数
        self.turn = config.coka_get_max_turn()
        ttt = self.turn[0][0]
        print(ttt)
        self.label_10.setText(str(ttt))

    def start(self):
        data = config.user_select_all()
        face_recognition.recognition(data)
