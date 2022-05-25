import _signal

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
import UI_User_Alter_Dialog
import config


class User_Alter_Dialog(QMainWindow, UI_User_Alter_Dialog.Ui_User_Alter_Dialog):
    _signal = QtCore.pyqtSignal(str)

    def __init__(self, id):
        super(User_Alter_Dialog, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.clicked_update(id))
        # 获取信息
        self.get_data(id)

    def clicked_update(self, id):
        sname = self.lineEdit.text()
        sno = self.lineEdit_2.text()
        college = self.lineEdit_3.text()
        config.user_update_by_id(id, sno, sname, college)
        self._signal.emit("refresh")
        self.close()

    def get_data(self, id):
        data = config.user_select_by_id(id)
        self.lineEdit.setText(data[1])
        self.lineEdit_2.setText(data[2])
        self.lineEdit_3.setText(data[3])
        print(data)
